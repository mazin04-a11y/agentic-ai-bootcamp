pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "crewai-app"
        GITHUB_REPO  = "${env.GITHUB_REPO ?: 'your-github-username/your-repo-name'}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest tests/ -v --tb=short || true'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest"
            }
        }

        stage('Push to GitHub') {
            steps {
                sh 'git config user.email "jenkins@ci.local"'
                sh 'git config user.name "Jenkins CI"'
                sh 'git push origin main'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded — Streamlit Cloud will auto-redeploy from GitHub.'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}
