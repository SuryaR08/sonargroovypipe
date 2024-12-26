pipeline {

    agent any

    stages {

        stage('Build') {

            steps {

                echo 'I am Building!'

            }

        }

        stage('Test') {

            steps {

               echo 'I am Testing!'

            }

        }

        stage('Deploy') {

            steps {

                echo 'I am Deploying!'

            }

        }

    }
  Post{
    success{
      echo 'Build Sucess!'
    }
    failure{
      echo 'Build Failed!'
    }
  }
}
