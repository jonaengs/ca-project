pipeline {
    agent { docker { image 'python:3-alpine' } }

    stages {
        stage('greetings') {
            steps{
                echo 'Hola Mundo!'
            }
        }
	stage('Preparation') {
	    steps{
		echo 'Preparation'
		sh 'pip install --user --upgrade pip'
		sh 'pip install --user -r requirements.txt'
	    }
	}
	stage('Build') {
	    steps{
		echo 'Build'
		sh 'python **/create_db.py'
	    }
	}
	stage('Results') {
	   steps{
		echo 'Results'
		sh 'python **/tests.py'
	   }
	}
    }
}
