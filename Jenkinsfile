pipeline {
    agent { docker { image 'python:3-alpine' } }

    stages {
	stage('Preparation') {
	    steps{
		echo 'Prep'
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
