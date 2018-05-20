# outlookApiSimplified
Python Wrapper around Outlook REST API 

## Installation (using docker)
(Its assumed that you have docker tools installed in your computer and you have registered your application at [Microsoft Application Portal](https://apps.dev.microsoft.com/) )
	
  1. Clone the project to a directory
  
  2. Add the client id to index.html and flaskServer.py (add your client secret to this file also). 
	
  3. In the docker console navigate to the project directory and run the following command.
  
      `docker build -t outlookapi:latest .`
  
      `docker run -d -t 5000:5000 outlookapi`
  
  4. Run index.html from the project directory 

  
