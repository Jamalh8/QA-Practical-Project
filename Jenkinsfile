pipeline {
    agent any
    stages {
        stage('Pytest') {         
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''sudo apt install python3 python3-pip python3-venv -y
                pip3 install pytest pytest-cov
                sudo chmod +x test.sh
                ./test.sh'''
            }
            stage('Deploy') {         
            steps {
                //
                sh '''scp  nginx_lb.conf jenkins@docker:/home/jenkins/
                docker start nginx
                scp  docker-compose.yaml jenkins@docker:/home/jenkins/
                docker stack deploy --compose-file docker-compose.yaml f1-stack'''
            }
        }
    }
}
