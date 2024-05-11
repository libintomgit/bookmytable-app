pipeline{
    // agent{
    //     label "node"
    // }
    agent any

    environment{
        // Add global environment here
        STAGE_1 = "Clone Repo"
        STAGE_2 = "Build Image"
        STAGE_3 = "Test Image"
        STAGE_4 = "Push Image"
        DOCKER_IMAGE_TAG = "libintomkk/bookmytable-fe-image:${BUILD_NUMBER}"
    }

    stages{
        stage("Clone Repo"){
            steps{
                // Step 1
                echo "This is stage - ${STAGE_1}"
                echo "Cloning the Repository"

                // Step 2
                // Checkout code from a Git repository
                // git branch: 'main', credentialsId: '', url: ''
                checkout scm
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Build Image"){
            steps{
                echo "Building the Image"
                // app = docker.build("libintomkk/bookmytable-fe-image")
                script{
                    docker.build "${DOCKER_IMAGE_TAG}"
                }
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Test Image"){
            steps{
                echo "Testing the image"
                // app.inside {
                //     sh 'echo "Test passed"'
                // }

            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Push Image"){
            steps{
                echo "Pushing image to docker hub"
                script{
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-libin') {
                        docker.image("${DOCKER_IMAGE_TAG}").push()
                    }                    
                }           
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Trigger Manifestupdate"){
            steps{
                echo "triggering updatemanifestjob"
                build job: 'bmt-fe-update-manifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
                }           
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}