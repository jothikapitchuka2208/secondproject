from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('base.html')
@app.route('/home')
def child():
    return render_template('child.html')
app.run(use_reloader=True)
