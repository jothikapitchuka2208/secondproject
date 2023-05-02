from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/fail')
def index():
    return 'you are failed'
@app.route('/input/<float:number>')
def user(number):
    if number >=35.0:
        return redirect(url_for('third'))
    else:
        return redirect(url_for('index'))
@app.route('/pass')
def third():
    return 'You are passed'
app.run(debug=True,use_reloader=True)

#url_for--->to build dynamic url
