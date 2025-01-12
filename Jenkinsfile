pipeline {
    agent any
    environment {
    PATH = "C:/Users/sp/AppData/Local/Programs/Python/Python313;C:/Users/sp/AppData/Local/Programs/Python/Python313/Scripts;C:/kubernetes;$PATH"
    DOCKERHUB_CREDENTIAL_ID = 'lab2-jenkins-dockerhub-token'
    DOCKERHUB_REGISTRY = 'https://registry.hub.docker.com'
    DOCKERHUB_REPOSITORY = 'leonovsp/lab2-project-calc'
    }
    stages {
        stage('Clone Repo') {
            steps {
                script {
                    echo 'Cloning GitHub Repository...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'lab2-git-token', url: 'https://github.com/vitaliikhai/lab1.git']])
                }
            }
        }
        stage('Add Timestamp') {
            steps {
                script {
                    def timestamp = new Date().format("yyyy-MM-dd HH:mm:ss")
                    bat """
                    echo Build #%BUILD_ID% at ${timestamp} >> .\\templates\\index.html
                    """
                }
            }
        }
        stage('Tests') {
            steps {
                //Lint test
                script {
                    echo 'Linting Python Code'
                // Для Linux/Unix систем
                //sh 'python --version'

                //  для Windows
                bat 'python --version'
                bat 'python -m pip install -r requirements.txt '
                bat 'pylint calc.py test_app.py --output=pylint-report.txt --exit-zero'
                bat 'type pylint-report.txt'
                bat 'flake8 calc.py test_app.py --ignore=E501,E302 --output-file=flake8-report.txt --exit-zero'
                bat 'type flake8-report.txt'
                bat 'black calc.py test_app.py'
                }
            }
        }
        stage('Run unittest') {
            steps {
                bat 'python -m unittest discover -s . -p "*.py"'
            }
        }
        stage('Trivy FS Scan') {
            steps {
                // Trivy Filesystem Scan
                script {
                    echo 'Scan Filesystem with Trivy'
                    bat 'trivy fs ./ --format table -o trivy-fs-report.html'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker Image
                script {
                    echo 'Building Docker Image'
                    dockerImage = docker.build("${DOCKERHUB_REPOSITORY}:latest")
                }
            }
        }
        stage('Trivy Docker Image Scan') {
            steps {
                // Trivy Docker Image Scan
                script {
                    echo 'Scanning Docker Image with Trivy.'
                    bat  "trivy image ${DOCKERHUB_REPOSITORY}:latest --format table -o trivy-docker-image-report.html"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                // Push Docker Image to DockerHub
                script {
                    echo 'Pushing Docker Image to DockerHub.'
                    docker.withRegistry("${DOCKERHUB_REGISTRY}", "${DOCKERHUB_CREDENTIAL_ID}"){
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Deploy Docker Container') {
            steps {
                script {
                    echo 'Deploying Docker Container on the local docker server.'
                    def containerName = DOCKERHUB_REPOSITORY.tokenize('/').last() // Витягуємо лише "lab2-project-calc"
                    bat """
                    docker stop ${containerName} || echo Container not running
                    docker rm ${containerName}
                    docker run -d --name ${containerName} -p 5000:5000 ${DOCKERHUB_REPOSITORY}:latest
                    """
                }
            }
        }
    }
}
