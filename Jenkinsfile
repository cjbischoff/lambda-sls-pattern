pipeline {
    agent {
        node {
            label 'docker'
        }
    }
    parameters {
        string(name: 'TEST_IMAGE_ID', defaultValue: 'lambda-sls-pattern-test', description: 'Test image name')
        string(name: 'IMAGE_ID', defaultValue: 'lambda-sls-pattern', description: 'Build image name')
    }
    stages {
        stage('Test') {
            steps {
                sh "docker build -f test/Dockerfile -t ${params.TEST_IMAGE_ID} ."
                sh "docker run -t ${params.TEST_IMAGE_ID}"
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t ${params.IMAGE_ID} ."
            }
        }

        stage('Release') {
            when { branch 'master' }

            steps {
                script {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'svcacct_uswest1-aws-dev-user']]) {
                        docker.image(params.IMAGE_ID).inside('-u root') {
                            sh 'serverless deploy --stage dev --region us-west-1 --serviceName lambda-sls-pattern'
                        }
                    }
                }
            }
        }
    }
}
