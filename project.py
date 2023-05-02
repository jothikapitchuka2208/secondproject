from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return 'welcome to application'
@app.route('/homepage')
def home():
    return render_template('index.html')
app.run()
