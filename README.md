REST API Flask
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
    
    
==================================================================================================================================================================================
