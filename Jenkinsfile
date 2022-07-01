pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''sudo apt install python3 python3-pip python3-venv -y
                pip3 install pytest pytest-cov
                sudo chmod +x test.sh
                ./test.sh'''
            }
        }
        stage('Deploy') {
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''scp  sudo docker-compose.yaml jamal@swarm-manager:/home/jamal
                sudo docker stack deploy --compose-file home/jamal/docker-compose.yaml f1-stack
                scp  nginx_lb.conf jamal@docker:/home/jamal
                sudo docker start nginx'''
            }
        }
        stage('Curl') {
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh 'curl docker'
            }
        }
    }
}
