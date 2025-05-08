pipeline {
    agent any

    environment {
        REGISTRY_CREDENTIALS = credentials('docker-hub')
        IMAGE_NAME = "yourdockerhubusername/flask-sample:${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pip install -r app/requirements.txt'
                sh 'pytest -q'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME ./app'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl set image deployment/flask-sample-deployment flask-sample=$IMAGE_NAME --record
                '''
            }
        }
    }

    post {
        failure {
            mail to: 'devops-team@example.com',
                 subject: "Pipeline FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Check console output at ${env.BUILD_URL}"
        }
    }
}
