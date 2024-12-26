pipeline {

    agent any

    stages {

        stage('Breakfast') {

            steps {

                echo 'Having breakfast!'

            }

        }

        stage('Workout') {

            steps {

                echo 'Doing my workout!'

            }

        }

        stage('Study') {

            steps {

                echo 'Studying and learning new things!'

            }

        }

        stage('Family Time') {

            steps {

                echo 'Spending quality time with family!'

            }

        }

        stage('Play') {

            steps {

                echo 'Playing volleyball and having fun!'

            }

        }

    }

    post {

        success {

            echo 'My day went well!'

        }

        failure {

            echo 'Something went wrong in my day!'

        }

    }

}
