from flask import Flask,render_template,request
import ibm_db
from db import *
app = Flask(__name__) #creating the Flask class object   
conn=ibm_db.connect(dbconnect(),"","") 
@app.route('/') #decorator drfines the   
def login():  
    return render_template("login.html")
msg=""
@app.route('/upload', methods=['POST']) 
def upload():
    
    
     username=request.form['username']
     password=request.form['password']
     sql="SELECT * FROM user WHERE username=? AND password=?"
     statement=ibm_db.prepare(conn,sql)
     ibm_db.bind_param(statement,1,username)
     ibm_db.bind_param(statement,2,password)
     ibm_db.execute(statement)
     acc=ibm_db.fetch_assoc(statement)
     if acc:
        return render_template("newspage.html")
     else:
        msg="Invalid username or password"
        return render_template("")

if __name__ =='__main__':  
    app.run(debug = True)  