# save this as app.py
import base64
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = b'JanusLePetit'

@app.route("/")
def start():
    if 'authentification' in session:
        if session['authentification'] == 1 :
            return render_template("index.html")
        else:  
            return render_template("login.html")
    else:  
        return render_template("login.html")

@app.route("/filter")
def rules_filter():
    if 'authentification' in session:
        if session['authentification'] == 1 :
            return render_template("rules_filter.html")
        else:  
            return render_template("login.html")
    else:  
        return render_template("login.html")
    

@app.route("/nat")
def rules_nat():
    if 'authentification' in session:
        if session['authentification'] == 1 :
            return render_template("rules_nat.html")
        else:  
            return render_template("login.html")
    else:  
        return render_template("login.html")
    

@app.route("/add")
def rules_nat_add():
    if 'authentification' in session:
        if session['authentification'] == 1 :
            return render_template("rules_nat.html")
        else:  
            return render_template("login.html")
    else:  
        return render_template("login.html")

@app.route("/alias")
def alias():
    if 'authentification' in session:
        if session['authentification'] == 1 :
            return render_template("alias.html")
        else:  
            return render_template("login.html")
    else:  
        return render_template("login.html")
    

@app.route("/login", methods=['POST'])
def login():
    login = request.form['username']
    password = request.form['password']
    hach = login +':'+ password
    hach = base64.b64encode(hach.encode('utf-8'))
    with open("mdp.txt", "r") as f:
        mdpbase = f.read()
    print(mdpbase)
    print(hach.decode('utf-8'))
    if mdpbase == hach.decode('utf-8') :
        session['authentification'] = 1
        return render_template('index.html')
    else :
        return render_template('login.html')