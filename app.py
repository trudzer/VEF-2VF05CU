from flask import Flask, flash, redirect, render_template, request, json, url_for, make_response, escape, session, abort
import pymysql
import os
import urllib.request
import pymysql.cursors
import pymysql

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8\n\xec]/'
print(os.urandom(16))

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0211982189', password='mypassword', database='0211982189_verk7')

@app.route('/')
def inndex():
    if not session.get('logged_in'):
        return render_template('index.tpl')
    else:
        return render_template('admin.tpl')

@app.route('/nyskra',methods=['GET', 'POST'])
def nyr():
    error = None
    if request.method == 'POST':
        userDetails = request.form
        user = userDetails['user_name']
        email = userDetails['user_email']
        password = userDetails['user_password']
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO 0211982189_verk7.users(user_name, user_email, user_password) VALUES(%s,%s,%s)",(user,email,password))
            conn.commit()
            cur.close()
            flash('Þú hefur verið skráður inn í gagnagrunninn')
            return redirect(url_for('users'))
        except pymysql.IntegrityError:
            error = 'Notandi er þegar skráður með þessu nafni og lykilorði'

        return render_template('index.tpl',error = error)

@app.route('/users')
def users():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT * FROM 0211982189_verk7.users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.tpl',userDetails=userDetails)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form.get('user_name')
        passw = request.form.get('user_password')

        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306,user='0211982189',password='mypassword')
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM 0211982189_verk7.users where user_name=%s and user_password=%s")
        result = cur.fetchone()
        print (result)

        if result[0] == 1:
            cur.close()
            conn.close()
            flash('Þú hefur verið skráður inn á vefsíðuna')
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            error = 'Innskráning mistókst - reyndu aftur'
    return render_template('index.tpl', error=error)

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return render_template('index.tpl')
    else:
        try:
            cur = conn.cursor()
            resultValue = cur.execute("SELECT * FROM 0211982189_verk7.users")
            if resultValue > 0:
                userDetails = cur.fetchall()
                flash('velkominn')
                return render_template('admin.tpl', userDetails=userDetails)
        except pymysql.IntegrityError:
            error = 'Þú hefur ekki aðgang að þessari síðu'
        return render_template('index.tpl')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return render_template('index.tpl')

@app.errorhandler(404)
def bad_request(error):
    return render_template('page_not_found.tpl'), 404

#@app.errorhandler(400)
#def bad_request(error):
#    return render_template('page_not_found.tpl'), 400

@app.route('/error')
def err():
    return render_template('error.tpl')

if __name__ == '__main__':
   app.run()
