pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building the project..."
                sh 'echo Build successful!'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'echo All tests passed!'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
            }
        }
    }
}
