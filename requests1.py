from flask import Flask,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return 'welcome to the application'
@app.route('/input/<name>/<place>')
def input(name,place):
    return redirect(url_for('second',user=name,city=place))
@app.route('/details')
def second():
    user=request.args.get('user')
    city=request.args.get('city')
    return f'hello,{user} you are in {city}'
app.run(debug=True,use_reloader=True)

