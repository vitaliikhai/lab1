pipeline {
    agent any
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
                    python --version
                }
            }
        }
    }
}
