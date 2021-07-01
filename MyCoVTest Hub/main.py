from validate_email import validate_email
from flask import Flask, render_template, jsonify, request, url_for, make_response, sessions, logging, session,g, redirect, flash
from mailbox import Message
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import sha256_crypt
import js2py
import mysql.connector
from flask_wtf.csrf import CSRFProtect
from wtforms import Form, BooleanField, TextField, PasswordField, validators
import os
import eel
import matplotlib.pyplot as plt

# initializing app
app = Flask(__name__)
app.secret_key=os.urandom(24)
# protecting our app

cnx = mysql.connector.connect(host="localhost",user="root", password="Anki1389", database="MWA_CW3", auth_plugin='mysql_native_password')
cursor=cnx.cursor()


@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/home')
def home():
    return render_template('Index.html')


@app.route('/Vhome', methods=["GET","POST"])
def Vhome():
    if "Vuser" in session:
        Vuser = session["Vuser"] 
        return render_template('Vhome.html')
    else:
        return redirect('login')

def Countgrpwise():
    sql_query1 = """select VassineGroup, TestResult,VassineGroupDose from VaccineDose,VaccineTestResult where VaccineDose.Email = VaccineTestResult.Email"""
    cursor.execute(sql_query1)
    arecord2 = cursor.fetchall()
    cnx.commit()
    print(arecord2)
    grpcnt=0
    grpcnt1=0
    for i in range(len(arecord2)):
        for j in range(len(arecord2[i])):
            if arecord2[i][j]=="A":
                if arecord2[i][j+1]=="Positive":
                    grpcnt+=1
    
    for i in range(len(arecord2)):
        for j in range(len(arecord2[i])):
            if arecord2[i][j]=="B":
                if arecord2[i][j+1]=="Positive":
                    grpcnt1+=1
    return grpcnt,grpcnt1

print(Countgrpwise())

        
    

@app.route('/Vmdash', methods=["GET","POST"])
def Vmdash():
    if 'Vmemail' in session:
        Vmuser = session["Vmemail"]
        sql_query = """select * from Volunteer"""
        cursor.execute(sql_query)
        arecord = cursor.fetchall()
        cnx.commit()
        num = len(arecord)
        sql_query1 = """select TestResult from VaccineTestResult"""
        cursor.execute(sql_query1)
        arecord2 = cursor.fetchall()
        cnx.commit()
        pcount=0
        for i in range(len(arecord2)):
            for j in range(len(arecord2[i])):
                if arecord2[i][j]=="Positive":
                    pcount+=1
        ncount=0            
        for i in range(len(arecord2)):
            for j in range(len(arecord2[i])):
                if arecord2[i][j]=="Negative":
                    ncount+=1
        if(pcount<10):            
            arr = Countgrpwise()
            return render_template('Vmdash.html', pcount=pcount, number=num, ncount=ncount, ap=arr[0], bp=arr[1])
        else:
            return render_template('Vmdash.html', pcount=pcount, number=num)
    else:
        return redirect('/')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        session.pop('Vuser', None)
        session.pop('email', None)
        user=request.form.get("login_username")
        password = str(request.form.get("login_password"))

        sql_query = """select * from Volunteer where Email = %s"""
        cursor.execute(sql_query,(user,))
        arecord = cursor.fetchall()
        cnx.commit()
        if (len(arecord)==0):
            flash("This email is not registered, Registere First.. !!", "danger")
            return redirect(url_for('register'))
        elif(len(arecord)==1):
            if user == arecord[0][0]:
                if sha256_crypt.verify(password, arecord[0][1]):
                    session['Vuser'] = arecord[0][2]
                    session['email'] = arecord[0][0]                    
                    sql_query1 = """select * from VaccineDose where Email = %s"""
                    cursor.execute(sql_query1,(user,))
                    arecord1 = cursor.fetchall()
                    cnx.commit()
                    
                    if (len(arecord1)==1):  
                        sql_query1 = """select * from VaccineTestResult where Email = %s"""
                        cursor.execute(sql_query1,(user,))
                        arecord2 = cursor.fetchall()
                        cnx.commit()
                        if (len(arecord2)==1):
                            flash("Volunteer Login Successful, You already registed Vaccine Dose so its Result too, Thank you for Participation", "success")                      
                            return redirect(url_for("done"))
                        else:
                            flash("Volunteer Login Successful, You already registed Vaccine Dose so, Now submit its Result", "success")                      
                            return redirect(url_for("submitresult"))
                    else:
                        flash("Volunteer Login Successful", "success")
                        return redirect(url_for("Vhome"))
                else:
                    flash("Invalid password for this username", "danger")
                    return render_template('Login.html') 
        else:
            flash("Something went wrong(Invalid Username or password)", "danger")
            return render_template('Login.html')
    return render_template('Login.html')
    

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        fname = request.form.get("fullname")
        age = request.form.get("age")
        gender = request.form.get("gender")
        postcode = request.form.get("postcode")
        add1 = str(request.form.get("first_line"))
        add2 = str(request.form.get("second_line"))
        add3 = str(request.form.get("third_line"))
        town = str(request.form.get("post_town"))
        fulladd = add1 +' '+ add2 +' '+ add3 +' '+ town +' '+ postcode
        chk = request.form.get("chk")
        pwd = request.form.get("pwd")
        cpwd = request.form.get("cpwd")

        sql_query = """select * from Volunteer where Email = %s"""
        cursor.execute(sql_query,(email,))
        arecord = cursor.fetchall()
        cnx.commit()
        if (len(arecord)==1):
            flash("This email is already registered, Use Different Email ID.. !!", "danger")
            return redirect(url_for('register'))
        elif pwd == cpwd:
            phash = sha256_crypt.encrypt(pwd)
            if chk == "yes":
                Hinfo = request.form.get("txtBox")
            else:
                Hinfo = "N/A"            
            #print (email, phash, fname, gender, age, fulladd, Hinfo)
            sql_query1 = """insert into Volunteer values (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql_query1, (email, phash, fname, gender, age, fulladd, Hinfo))
            print(cursor.rowcount, "record(s) affected")
            cnx.commit()
            flash("Volunteer Successfully Registered. You can Login Now..!!", "success")
            return redirect(url_for('login'))
        else:
            flash("Password and confirm Password mismatch..!!", "success")
            return redirect(url_for('login'))
                    
    return render_template('Register.html')

@app.route('/Vlogin',methods=["GET","POST"])
def Vlogin():
    if request.method == "POST":
        session.pop('Vuser', None)
        session.pop('email', None)
        user=request.form.get("login_username")
        password = str(request.form.get("login_password"))

        sql_query = """select * from VaccineMaker where Email = %s"""
        cursor.execute(sql_query,(user,))
        arecord = cursor.fetchall()
        cnx.commit()
        if (len(arecord)==0):
            flash("This email is not registered, Registere First.. !!", "danger")
            return redirect(url_for('Vlogin'))
        elif(len(arecord)==1):
            if user == arecord[0][0]:
                if sha256_crypt.verify(password, arecord[0][1]):
                    session['Vmemail'] = arecord[0][0]                    
                    flash("Vaccinemake Login Successful...!!!", "Success")
                    return redirect(url_for('Vmdash'))
                else:
                    flash("Invalid password for this username", "danger")
                    return render_template('Vlogin.html') 
        else:
            flash("Something went wrong(Invalid Username or password)", "danger")
            return render_template('Vlogin.html')
    
    return render_template('Vlogin.html')

@app.route('/vaccinegrp',methods=["GET","POST"])
def vaccinegrp():
    if request.method == "POST":
        vgrp = request.form.get("vgrp")
        vgrpdose = request.form.get("vgrpdose")
        if "email" in session:
            email = session["email"]
            sql_query = """select * from VaccineDose where Email = %s"""
            cursor.execute(sql_query,(email,))
            arecord = cursor.fetchall()
            if (len(arecord)==0):
                sql_query1 = """insert into VaccineDose values (%s, %s, %s)"""
                cursor.execute(sql_query1, (email, vgrp, vgrpdose))
                print(cursor.rowcount, "record(s) affected")
                cnx.commit()
                flash("Volunteer Successfully added Vaccine dose taken..!!", "success")
                return redirect('submitresult')
            else:
                flash("Volunteer not Successfully added Vaccine dose taken..!!", "danger")
                return redirect('vaccinegrp')
    return render_template('vaccinegrp.html')

@app.route('/submitresult',methods=["GET","POST"] )
def submitresult():
    if "Vuser" in session:
        Vuser = session["Vuser"] 
        if request.method == "POST":
            rgrp = request.form.get("rgrp")
            if "email" in session:
                email = session["email"]            
                sql_query = """select * from VaccineTestResult where Email = %s"""
                cursor.execute(sql_query,(email,))
                arecord = cursor.fetchall()
                cnx.commit()
                if (len(arecord)==0):
                    sql_query1 = """insert into VaccineTestResult values (%s, %s)"""
                    cursor.execute(sql_query1, (email, rgrp))
                    print(cursor.rowcount, "record(s) affected")
                    cnx.commit()
                    flash("Volunteer Successfully added Vaccine Dose and the TestResult of taken Vaccine dose..!! Can Logout Now..!!", "success")
                    return redirect(url_for('done'))
                else:
                    flash("Volunteer not Successfully added TestResult of taken Vaccine dose..!!", "danger")
                    return redirect(url_for('submitresult'))
    return render_template('Submitresult.html')

@app.route('/qrcode')
def qrcode():
    return render_template('Qrcode.html')

@app.route('/last')
def last():
    return render_template('last.html')   


@app.route('/done')
def done():
    return render_template('done.html')

@app.route('/Vlogout')
def Vlogout():
    if "Vuser" in session:
        session.pop('Vuser')
        if "email" in session:
            session.pop("email")
    return redirect('login')

@app.route('/Vmlogout')
def Vmlogout():
    session.pop('Vmemail')
    return redirect("Vlogin")



if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)




