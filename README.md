REST API Flask
=================================================================================================================================================================================

This project was implemented to implement a quick RESTful API through Flask Framework. No CSS or JS was used to style the Templates as the primary purpose of this project was to 
implement HTTP Methods efficiently.
To store and process data, a JSON file was considered as sample storage and the JSON module is used to handle the methods based on the information passed.
The following HTTP Methods were implemented:
    1. GET
    2. POST
    3. PUT
    4. PATCH
    5. DELETE
Basically it was meant to process CRUD methods.

 
How to setup and run the server?
==================================================================================================================================================================================


Before Installing Flask please consider using a Virtual Environment.
[ALL COMMANDS ON THIS FILE ARE TO BE EXECUTED ON CLI UNTIL EXPLICITLY MENTIONED OTHERWISE. ]
To create a virtual Environment, follow the steps mentioned below:
    1. In your Command Line, Make sure your Python can be activated(Add it to your PATH)
    2. Create A New Directory as per your working prefernce
    3. Outside the working directory execute the following command:
       ``` python -m  venv virtualenv ```
    4. The requirements have been attached to this project, as requirements.txt
       For your convenience you can run the same requirements or manually install packages using pip 
    5. If you are using Windows and are developing your HTTP server:
        Set FLASK_ENV=development
        Set FLASK_APP=app.py
       If you are using Linux/Apple OS:
        ```Export FLASK_ENV=development
        Export FLASK_APP=app.py```
    6. Remove the if __name__ == "__main__" part in app.py before running if you want to modify and run.
    7.  There are other features in Flask which can be accessed in their docs:   
        Https://flask.palletsprojects.com/en/2.0.x/
    7. To run the Flask server:
           ``` Flask run -p <address>:<port>```
 
