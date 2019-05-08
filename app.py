from flask import Flask, flash, redirect, render_template, request, json, url_for, make_response, escape, session, abort
import pymysql
import os
import urllib.request
import pymysql.cursors
import pymysql

app = Flask(__name__)
app.secret_key = os.urandom(16)
print(os.urandom(16))

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0211982189', password='mypassword', database='0211982189_lokaverkefni')

@app.route('/')
def inndex():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT postur FROM 0211982189_lokaverkefni.posts;")
    if resultValue > 0:
        userDetails = cur.fetchall()
        flash('Velkominn')
        return render_template('index.tpl', userDetails=userDetails)

@app.route('/nyskra',methods=['GET', 'POST'])
def nyr():
    error = None
    if request.method == 'POST':
        userDetails = request.form
        userID = userDetails['userID']
        user = userDetails['user_name']
        email = userDetails['user_email']
        password = userDetails['user_password']
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO 0211982189_lokaverkefni.users(userID, user_name, user_email, user_password) VALUES(%s,%s,%s,%s)",(userID,user,email,password))
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
    resultValue = cur.execute("SELECT * FROM 0211982189_lokaverkefni.users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.tpl',userDetails=userDetails)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        admin_user = request.form.get('admin_name')
        admin_passw = request.form.get('admin_password')
        user = request.form.get('user_name')
        passw = request.form.get('user_password')

        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306,user='0211982189',password='mypassword',database='0211982189_lokaverkefni')
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM 0211982189_lokaverkefni.users where user_name=%s and user_password=%s",(user, passw))
        result = cur.fetchone()
        print (result)

        if result[0] == 1:
            cur.close()
            conn.close()
            flash('Þú hefur verið skráður inn á vefsíðuna')
            session['logged_in'] = True
            return render_template('users.tpl', users=users)
        else:
            error = 'Innskráning mistókst - reyndu aftur'
    return render_template('index.tpl', error=error)

@app.route('/change', methods=['GET', 'POST'])
def edit():
    if not session.get('logged_in'):
        return render_template('index.tpl')
    error = None
    if request.method == 'POST':
        user = request.form.get('userID')
        try:
            cur = conn.cursor()
            result = cur.execute("SELECT * FROM 0211982189_lokaverkefni.posts WHERE userID=%s",(user))
            if result > 0:
                userDetails = cur.fetchall()
                flash('Veldu póstnúmer')
                return render_template('change.tpl', userDetails=userDetails)
        except pymysql.IntegrityError:
            error = 'Þú hefur ekki aðgang að þessari siðu'
        return render_template('index.tpl')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return render_template('index.tpl')
    else:
        try:
            cur = conn.cursor()
            resultValue = cur.execute("SELECT * FROM 0211982189_lokaverkefni.users")
            if resultValue > 0:
                userDetails = cur.fetchall()
                flash('velkominn')
                return render_template('admin.tpl', userDetails=userDetails)
        except pymysql.IntegrityError:
            error = 'Þú hefur ekki aðgang að þessari síðu'
        return render_template('index.tpl')

@app.route('/new_post', methods=['GET', 'POST'])
def news():
    if not session.get('logged_in'):
        return render_template('index.tpl')
    else:
        session['logged_in'] = True
    error = None
    if request.method == 'POST':
        pi = request.form.get('postID')
        po = request.form.get('postur')
        ui = request.form.get('userID')

        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306,user='0211982189',password='mypassword',database='0211982189_lokaverkefni')
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM 0211982189_lokaverkefni.users WHERE userID=%s",(ui))
        result = cur.fetchone()
        print(result)

        if result[0] == 1:
            cur.execute("INSERT INTO 0211982189_lokaverkefni.posts VALUES(%s,%s,%s)",(pi,po,ui))
            conn.commit()
            print(result)
            cur.close()
            conn.close()
            flash('Nýr póstur hefur verið skráður')
            cur.execute("SELECT postur FROM 0211982189_lokaverkefni.posts")
            return render_template('users.tpl',pi=pi)
        else:
            error = 'Nýskráning mistókst'
    return render_template('users.tpl', error=error)

@app.route('/changePost/<int:id>')
def editpost(id):
    try:
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0211982189', password='mypassword', database='0211982189_lokaverkefni')
        cur = conn.cursor()
        cur.execute("SELECT * FROM 0211982189_lokaverkefni.posts WHERE postID=%s", id)
        conn.commit()
        result = cur.fetchall()
        print(result)
        if result:
            return render_template('changePost.tpl', result=result)
        else:
            return 'Error loading #{id}'
    finally:
            cur.close()
            conn.close()

@app.route('/changed/', methods=['GET', 'POST'])
def post():
    if not session.get('logged_in'):
        return render_template('index.tpl')

    pi = request.form.get('postID')
    po = request.form.get('postur')
    ui = request.form.get('userID')

    button = request.form.get('breyta')
    if button == 'Breyta':
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0211982189', passwd='mypassword', db='0211982189_lokaverkefni')
        cur = conn.cursor()
        cur.execute("UPDATE 0211982189_lokaverkefni.posts SET postur=%s WHERE postID=%s AND userID=%s", (po, pi, ui))
        conn.commit()
        print(cur)
        cur.close()
        conn.close()
        flash('Póstinum hefur verið breytt í gagnagrunninn')
        session['logged_in'] = True
        return render_template('users.tpl')
    else:
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0211982189', passwd='mypassword', db='0211982189_lokaverkefni')
        cur = conn.cursor()
        cur.execute("Delete FROM 02119821809_lokaverkefni.posts WHERE postID=%s",(pi))
        conn.commit()
        cur.close()
        conn.close()
        flash('Póstinum hefur verið eytt úr gagnagrunninum')
        return render_template('users.tpl')

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
   app.run(debug = True)