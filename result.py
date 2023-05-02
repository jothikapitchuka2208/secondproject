from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return 'welcome to application'
@app.route('/homepage',methods=['GET','POST'])
def home():
  if request.method=="POST":  
    print(request.form)
    user=request.form['name']
    Python=int(request.form['Python'])
    MYSQL=int(request.form['MYSQL'])
    HTML=int(request.form['HTML'])
    
    return render_template('result.html',user=user,Python=Python,MYSQL=MYSQL,HTML=HTML)
  else:  
   return render_template('index.html')
app.run(use_reloader=True)
