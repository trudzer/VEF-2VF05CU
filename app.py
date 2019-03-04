from flask import Flask, redirect, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('form.tpl')

'''
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("namskeid2.tpl",result = result)
'''

@app.route('/data', methods = ['POST'])
def gogn():
   if(request.method == 'POST'):
      kwargs={
         'name': request.form['nafn'],
         'home': request.form['heimili'],
         'email': request.form['email'],
         'phone': request.form['simi'],
         'food': request.form['matur'],
         'course': request.form.getlist('namsk'),
      }

      sum = 0
      for item in request.form.getlist('namsk'):
         sum += 4000

      sum = sum
      sumMVsk = 1.24*sum

      return render_template('namskeid.tpl',**kwargs,sum=sum,total=sumMVsk)

@app.errorhandler(404)
def page_not_found(error):
   return render_template(page_not_found.tpl),404


if __name__ == '__main__':
   app.run()
