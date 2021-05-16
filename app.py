from flask import Flask,render_template as render, abort, request, jsonify 


app = Flask(__name__,template_folder='./templates')

@app.route('/GETPage',methods = ['GET'])
def Gpage():
    return 'You have landed on the page which allows the GET methods'

@app.route('/POSTPage', methods = ['GET','POST'])
def Ppage():
    if request.method == "POST":
        print(request.form)
        '''
        USE your model logic to write it to database
        '''
        return render('SuccessPage.html')
    else:
        return render('form.html')

@app.route('/MultiMethodPage', methods = ['GET','POST', 'PUT','PATCH', 'DELETE'])
def MethodsPage():
    return "Multiple Methods can be used here according to your python logic"
