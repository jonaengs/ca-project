pipeline {
    agent { docker { image 'python:3.5.1' } }

    stages {
        stage('greetings') {
            steps{
                echo 'Hola Mundo!'
            }
        }
	stage('Preparation') {
	    steps{
		echo 'Preparation'
		sh 'sudo pip install --upgrade pip'
		sh 'sudo pip install -r requirements.txt'
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
