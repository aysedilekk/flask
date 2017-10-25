from flask import Flask, jsonify, render_template, request
import requests
import json

app = Flask(__name__)
 
@app.route('/')
def index():
		return render_template('index.html')

@app.route('/echo/', methods=['GET', 'POST'])
def echo():
		if request.method == 'GET':
			ret_data = {"value": request.args.get('echoValue')}
			print ret_data
			return jsonify(ret_data)
		elif request.method == 'POST':
			ret_data = {"value": request.args.get('echoValue')}
				print ret_data
			return requests.post("http://127.0.0.1:8001", json=ret_data)

class person():
		def __init__(self, uuid, os, ip, browser):
			self.uuid = uuid
			self.os = os
			self.ip = ip
			self.browser = browser

@app.route('/new', methods = ['GET', 'POST'])
def new():
		if request.method == 'POST':
			if not request.form['uuid'] or not request.form['os'] or not request.form['ip'] or not request.form['browser']:
				flash('Please enter all the fields', 'error')
			else:
				student = person(request.form['uuid'], request.form['os'],request.form['ip'], request.form['browser'])
				
				students_list = {'uuid': student.uuid,
													'os': student.os,
													'ip': student.ip,
													'browser' : student.browser }

				 requests.post("http://127.0.0.1:8001", json=students_list)
				
	 return render_template('new.html')
	
		

if __name__ == '__main__':
		app.run(port=8000, debug=True) 
