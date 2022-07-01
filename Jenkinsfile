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
                sh '''scp docker-compose.yaml jamal@swarm-manager:/home/jamal/
                scp nginx.conf jamal@swarm-manager:/home/jamal/
                ssh jamal@swarm-manager sudo chmod +x docker-compose.yaml
                ssh jamal@swarm-manager docker stack deploy --compose-file docker-compose.yaml f1-stack
                scp nginx_lb.conf jamal@docker:/home/jamal/
                ssh jamal@docker docker run -d -p 80:80 --name nginx --mount type=bind,source=home/jamal/nginx_lb.conf,target=/etc/nginx/nginx.conf nginx '''
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
