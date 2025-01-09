pipeline {
    agent any
    environment {
    PATH = "C:/Users/sp/AppData/Local/Programs/Python/Python313;C:/Users/sp/AppData/Local/Programs/Python/Python313/Scripts;$PATH"
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
                bat 'flake8 calc.py test_app.py --ignore=E501,E302 --output-file=flake8-report.txt'
                bat 'black alc.py test_app.py'
                }
            }
        }
    }
}
