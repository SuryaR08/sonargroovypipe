pipeline{
  agent any
  environment{
    PYTHON_PATH='C:\Program Files\Python313;C:\Program Files\Python313\Scripts'
  }
  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('Build'){
      steps{
        bat '''
        set PATH=%PYTHON_PATH%;%PATH%
        pip install -r requirements.txt
        '''
      }
    }
    stage('SonarAnalysis'){
      environment{
        SONAR_TOKEN=credentials('sonarqube-token')
      }
      steps{
        bat '''
        set PATH=%PYTHON_PATH%;%PATH%
        sonar-scanner -Dsonar.projectKey=sonargroovy ^
        -Dsonar.projectName=sonargroovy ^
        -Dsonar.sources=. ^
        -Dsonar.host.url=http://localhost:9000 ^
        -Dsonar.token=sqp_b5d4456f8d766d8a680c3edef04d62128af807ee ^
        '''
      }
    }
  }
  post{
    success{
      echo 'Build Succeeded!'
    }
    failure{
      echo 'Build Failed'
    }
  }
}
