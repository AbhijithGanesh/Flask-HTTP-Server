REST API Flask

Before Installing Flask please consider using a Virtual Environment.
[ALL COMMANDS ON THIS FILE ARE TO BE EXECUTED ON CLI UNTIL EXPLICITLY MENTIONED OTHERWISE. ]
To create a virtual Environment, follow the steps mentioned below:
    1. In your Command Line, Make sure your Python can be activated(Add it to your PATH)
    2. Create A New Directory as per your working prefernce
    3. Outside the working directory execute the following command:
        python -m  venv VirtualEnv
    4. The requirements have been attached to this project, as requirements.txt
       For your convenience you can run the same requirements or manually install packages using pip 
    5. Installing the requirements using pip
        pip install -r requirements.txt
    6.  Your requirements should be installed.
    7. If you are using Windows and are developing your HTTP server:
        set FLASK_ENV=development
        set FLASK_APP=app.py
       If you are using Linux/Apple OS:
        export FLASK_ENV=development
        export FLASK_APP=app.py
    8.  There are other features in Flask which can be accessed in their docs:   
        https://flask.palletsprojects.com/en/2.0.x/
    9. To run the Flask server:
            flask run -p <address>:<port>


TO USE A DATABASE REFER TO MODELS.PY
THERE ARE ENNUMEROUS WAYS TO USE A  DATABSE
TWO SIMPLE CASES WOULD BE:
    1. SQLTIE
You can install sqlite using the following command (on your terminal/command prompt):
    pip install db-sqlite3

DB.SQLITE files are small-size databases and they can conviently store data according to your use case.
The sqlite3 package will provide an API which translates SQL strings in Python to SQL Language and execute it.
It works on the DB-API. For more info read: https://www.python.org/dev/peps/pep-0249/

If you insist on using a small sized easy-to-handle filesystem, you can use JSON as your file to store data
Simple Code Syntax can be found on JSON.py and SQLITE .py respectively

JSON module is a default package in Python 3, You need not install it with pip.