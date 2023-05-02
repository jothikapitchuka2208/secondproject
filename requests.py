from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def index():
    return 'welcome to the application'
@app.route('/second')
def second():
    print(request.method)
    print(request.args.get('user'))
    return 'i am in codegnan'
app.run(debug=True,use_reloader=True)

