pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.9-bullseye' 
                }
            }
            steps {
                sh "python main.py --diretorio_arquivos '/usr/src/rfb-cnpj/download' --database_url 'postgresql://postgres:postgres@localhost:5436/rfb_cnpj' " 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}