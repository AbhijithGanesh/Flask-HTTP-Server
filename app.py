from flask import Flask,render_template as render, request 
from models import *



app = Flask(__name__,template_folder='./templates')


@app.route('/GETPage',methods = ['GET'])
def Gpage():
    return f"You have landed on the page which allows the {request.method} method."

@app.route('/POSTPage', methods = ['GET','POST'])
def Ppage():
    if request.method == "POST":
        WriteModelJson(dict(zip(dict(request.form).keys(), dict(request.form).values())))
        return render('SuccessPage.html')
    else:
        return render('form.html')

@app.route('/MultiMethodPage', methods = ['GET','PUT','PATCH', 'DELETE'])
def MethodsPage():
    import json
    if request.method == "DELETE":
        data = json.loads(request.data)
        message =  DeleteJsonModel(data)
        return f"The Method used was: {request.method}\n  {message}"
    
    elif request.method == 'PUT':     
        data = json.loads(request.data)
        message = PutModelJson(data)
        return f"The Method used was: {request.method}\n  {message}"

    elif request.method == 'PATCH':
        message = PatchModelJson(json.loads(request.data))
        return f"The Method used was: {request.method}\n {message}"


    
    return "This page/URL supports PUT,PATCH and DELETE Methods. Use Postman to send in requests. "

if __name__ == "__main__":
    app.run()
