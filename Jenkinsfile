pipeline {
    agent any
    
    environment {
        GIT_CREDENTIALS = credentials('github-token') // Esto referencia el ID de las credenciales
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Usar el token para realizar el checkout del repositorio
                git url: 'https://github.com/HectorInove/g-challenge.git',
                    credentialsId: 'github-token', 
                    branch: 'main'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
