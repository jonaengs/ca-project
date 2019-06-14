pipeline {
    agent any

    stages {
	stage('Preparation') {
	    steps{
		echo 'Prep'
	    }
	}
	stage('Build') {
	    steps{	
		echo 'Build'
		sh 'docker build -t mygiraff .'
	    }
	}
	stage('Test') {
	   steps{
		echo 'Test'
		sh 'docker run mygiraff python $(pwd)/tests.py'
	   }
	}
    }
}
