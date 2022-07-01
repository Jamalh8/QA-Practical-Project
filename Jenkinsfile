pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDS_USR = credentials('dockerhub_id')
        DOCKER_HUB_CREDS_PSW = credentials('dockerhub_id')
    }
    stages {
        // stage('Test') {
        //     steps {
        //         //
        //         git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
        //         sh '''sudo apt install python3 python3-pip python3-venv -y
        //         pip3 install pytest pytest-cov
        //         sudo chmod +x test.sh
        //         ./test.sh'''
        //     }
        // }
        stage('Build Images') {
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''cd car-api/
                docker build -t jamalh8/cars-generator:latest .
                docker tag jamalh8/cars-generator:latest jamalh8/cars-generator:$BUILD_NUMBER
                cd ../driver-api/
                docker build -t jamalh8/cars-driver:latest .
                docker tag jamalh8/cars-driver:latest jamalh8/cars-driver:$BUILD_NUMBER
                cd ../front-end/
                docker build -t jamalh8/cars-front:latest 
                docker tag jamalh8/cars-front:latest jamalh8/cars-front:$BUILD_NUMBER
                cd ../rating-api/
                docker build -t jamalh8/cars-rating:latest
                docker tag jamalh8/cars-rating:latest jamalh8/cars-rating:$BUILD_NUMBER'''  
            }
        }
        stage('Docker login') {
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''ssh jamal@swarm-manager docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW
                ssh jamal@swarm-manager echo "logged into dockerhub"'''
            }
        }
        stage('Deploy') {
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''scp docker-compose.yaml jamal@swarm-manager:/home/jamal/
                scp nginx.conf jamal@swarm-manager:/home/jamal/
                ssh jamal@swarm-manager docker stack deploy --compose-file docker-compose.yaml f1-stack
                sleep 25'''
            }
        }
        stage('Curl') {
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''curl swarm-manager
                curl swarm-worker'''
            }
        }
    }
}
