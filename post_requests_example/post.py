from flask import Flask, request, flash, url_for, redirect, render_template
import requests
import json

app = Flask(__name__)

class students():
   def __init__(self, name, city, addr, pin):
	  self.name = name
	  self.city = city
	  self.addr = addr
	  self.pin = pin

@app.route('/', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
	  if not request.form['name'] or not request.form['city'] or not request.form['addr']:
		 flash('Please enter all the fields', 'error')
	  else:
		 student = students(request.form['name'], request.form['city'],
			request.form['addr'], request.form['pin'])
		 
		 students_list = {'name': student.name,
		 				  'city': student.city,
		 				  'addr': student.addr,
		 				  'pin' : student.pin }

		 requests.post("http://192.168.212.13/kisiler", json=students_list)
		 
   return render_template('new.html')

if __name__ == '__main__':
   app.run(debug = True)
