
from flask import Flask,render_template,request
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
         return render_template('home.html')
@app.route('/enternew')
def new_student():
         return render_template('student.html')
@app.route('/addrec',methods=['POST','GET'])
def addrec():
        if request.method=='POST':
            try:
               nm=request.form['nm']
               Address=request.form['add']
               City=request.form['city']
               PinCode=request.form['pin']
                  
               with sql.connect("data.db") as con:
                    cur=con.cursor()
                    cur.execute("INSERT INTO students(Name,Address,City,PinCode)VALUES(?,?,?,?)",(nm,Address,City,PinCode))
                    con.commit()
                    msg="Record successfully added"
            except:
                con.rollback()
                msg="error in insert operation "

            finally:
                return render_template("result.html",msg=msg)
                con.close()
@app.route('/list')
def list():
        con=sql.connect("data.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        return render_template("list.html",rows=rows)
#update


if __name__=='__main__':
           app.run(debug=True)