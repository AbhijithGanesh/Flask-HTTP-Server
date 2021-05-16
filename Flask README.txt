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
            flask run <port>
