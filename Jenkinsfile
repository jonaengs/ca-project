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
		sh 'docker run mygiraff python /usr/src/app/tests.py'
	   }
	}
	stage('Deploy') {
		steps{
			echo 'Deploy'
			sh 'docker container run -p 80:5000 -d mygiraff python /usr/src/app/run.py'			
		}
	}
    }
}
