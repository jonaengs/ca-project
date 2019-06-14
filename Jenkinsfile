pipeline {
    agent any

    stages {
        stage('greetings') {
            steps{
                echo 'Hola Mundo!'
            }
        }
	stage('Preparation') {
	    steps{
		echo 'Preparation'
		pip 'install -r requirements.txt'
	    }
	}
	stage('Build') {
	    steps{
		echo 'Build'
		python '**/create_db.py'
	    }
	}
	stage('Results') {
	   steps{
		echo 'Results'
		python '**/tests.py'
	   }
	}
    }
}
