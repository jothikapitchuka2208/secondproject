from flask import Flask,redirect
app=Flask(__name__)
@app.route('/')
def index():
    return 'iam in first page'
@app.route('/input/<float:number>')
def user(number):
    print(type(number))
    return f'the number entered is {number}'
@app.route('/pass')
def third():
    return 'You are passed'
app.run(debug=True,use_reloader=True)
