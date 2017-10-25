from flask import Flask, jsonify, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/new', methods = ['GET', 'POST'])
def new():
	if request.method == 'POST':
		student = person(request.form['uuid'], request.form['os'],request.form['ip'], request.form['browser'])
		students_list = {'uuid': student.uuid,'os': student.os,'ip': student.ip,'browser' : student.browser }
		return students_list
	return render_template('new.html')




if __name__ == '__main__':
	app.run(port=8001, debug=True) 
