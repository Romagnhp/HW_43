from flask import Flask, render_template, send_file, redirect
import datetime

obj_Flask = Flask(__name__)

userDictionary = {
    'goncharov': {
        'name':'Honcharov Roman', 
        'phoneNumber':'099-248-47-98', 
        'mail':'romagnhp@gmail.com'
        },
    'kalyuzhny': {
        'name':'Kalyuzhny Nikolai', 
        'phoneNumber':'099-248-47-91', 
        'mail':'kalyuzhny@gmail.com'
        },
}

def myStyle():
    t = datetime.datetime.now().hour
    if 6 <= t < 17:
        return 'css/styleWhite.css'
    else:
        return 'css/styleBlack.css'

@obj_Flask.route("/")
def homePage():
    return send_file("static/home.html")

@obj_Flask.route("/<secondName>")
def lounch_Rezume(secondName):
    if secondName in userDictionary:
        return render_template("/index.html", **userDictionary[secondName], cssPath = myStyle())
    else:
        return redirect("static/404.html")

@obj_Flask.route("/error")
def error():
    return send_file("static/404.html")

obj_Flask.run() 