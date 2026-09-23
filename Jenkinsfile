pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Changed from 'sh' to 'bat' for Windows execution
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build and Test') {
            steps {
                // Changed from 'sh' to 'bat' for Windows execution
                bat 'python -m pytest test_app.py'
            }
        }
    }
}
