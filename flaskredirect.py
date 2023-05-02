from flask import Flask,redirect
app=Flask(__name__)
@app.route('/fail')
def index():
    return 'iam in first page'
@app.route('/input/<float:number>')
def user(number):
    if number >=35.0:
        return redirect('http://127.0.0.1:5000/pass')
    else:
        return redirect('http://127.0.0.1:5000/fail')
@app.route('/pass')
def third():
    return 'You are passed'
app.run(debug=True,use_reloader=True)
