pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDS_USR = credentials('DOCKER_HUB_USR')
        DOCKER_HUB_CREDS_PSW = credentials('DOCKER_HUB_PSW')
    }
    stages {
        stage('Test') {
            steps {
                //
                git branch: 'main', credentialsId: 'bd42fab1-6db5-49a3-bf99-7e52de6e500b', url: 'git@github.com:Jamalh8/QA-Practical-Project.git'
                sh '''sudo chmod +x test.sh
                ./test.sh'''
            }
        }
        stage('Ansible - Infastructure creation') {
            steps {
                //
                git branch: 'main', credentialsId: 'bd42fab1-6db5-49a3-bf99-7e52de6e500b', url: 'git@github.com:Jamalh8/QA-Practical-Project.git'
                sh 'ssh jamal@gcp-dev-server \'/home/jamal/.local/bin/ansible-playbook -i QA-Practical-Project/config/inventory.yaml QA-Practical-Project/config/playbook.yaml\''
            }
        }
        stage('Docker-login, build, and push ') {
            steps {
                //
                git branch: 'main', credentialsId: 'bd42fab1-6db5-49a3-bf99-7e52de6e500b', url: 'git@github.com:Jamalh8/QA-Practical-Project.git'
                sh '''docker-compose build
                docker login --username $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW
                docker-compose push'''
            }
        }
        stage('Deploy') {
            steps {
                //
                git branch: 'main', credentialsId: 'bd42fab1-6db5-49a3-bf99-7e52de6e500b', url: 'git@github.com:Jamalh8/QA-Practical-Project.git'
                sh '''scp docker-compose.yaml jamal@swarm-manager:/home/jamal/
                scp nginx.conf jamal@swarm-manager:/home/jamal/
                ssh jamal@swarm-manager docker stack deploy --compose-file docker-compose.yaml f1-stack
                '''
            }
        }
        stage('Start-Nginx-lb') {
            steps {
                //
                git branch: 'main', credentialsId: 'bd42fab1-6db5-49a3-bf99-7e52de6e500b', url: 'git@github.com:Jamalh8/QA-Practical-Project.git'
                sh 'ssh jamal@nginx-lb ./nginx-lb-script.sh'
            }
        }
    }
}

