pipeline {
    agent any
    stages {
        stage('Pytest') {         
            steps {
                //
                git branch: 'feature/jenkinsfile', url: 'https://github.com/Jamalh8/QA-Practical-Project.git'
                sh '''sudo apt install python3 python3-pip python3-venv -y
                python3 -m venv venv
                source $env_name/bin/activate
                pip3 install -r requirements.txt
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
