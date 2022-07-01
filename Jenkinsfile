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
    //     }
    //     stage('Deploy') {
    //         }            
    //         steps {
    //             //
    //             git branch: 'dev', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
    //             sh '''#!/bin/bash
    //             if [ -f  /tmp/gpidfile ]
    //               then kill $(cat /tmp/gpidfile)
    //             fi
    //             source venv/bin/activate
    //             JENKINS_NODE_COOKIE=nokill gunicorn application:app -D -w 4 -b 0.0.0.0:5000 -p /tmp/gpidfile'''
            // }
        }
    }
}
