# **URL-Shortener**

This is a simple flask-react app which takes an URL and shortens it. This shortened verion of the URL redirects to the user to the long URL.

For each long URL given by the user the application randomly generates an alphabetical combination which redirects to the long URL.
#
Before starting the app, we might have to run some commandline (assuming we already have python3 and nodeJS installed)

  - pip3 install virtualenv 
  
  - source flask-server/venv/bin/activate
  
To start the Flask backend:
  - python3 flask-server/app.py  

To start the React frontend, change directory to the react-front file:
  - npm start
#
# Application will be accessed via after starting up flask and react:
##  http://localhost:3000/


#
# Future works:
  - Error handling for non-url inputs
  - Page styling, CSS etc.
  - Returning all exisiting urls that were shortened previously in a table format
  - Containerization (Docker)
  - Non-Flask Database (PostgreSQL)
  
