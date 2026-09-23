pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pulls the code from your GitHub main branch
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // For Windows nodes, change 'sh' to 'bat'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build and Test') {
            steps {
                // Runs your Python test suite
                sh 'pytest' 
            }
        }
    }
}
