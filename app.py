# mrparkonline
# Flask App Test
# initiative project

''' To Run:
1. python3 -m flask run
2. export FLASK_APP=filename.py --> flask run
'''

# import lines
from flask import Flask
from flask import render_template
from flask import request
import datetime

# data import
from data import TestMonster
from rows import Rows
from rows import addRow

app = Flask(__name__)

Test = TestMonster()
Rows = Rows()

@app.route('/')
def index():
	return render_template('home.html', monsters = Test)

@app.route('/test', methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		result = request.form
		Rows.append(addRow(result))
		# some ways to improve this:
		'''
		use of redirect and creating a class for our rows and database.
		implement mongodb pymongo
		'''

		return render_template('test.html', rows=Rows, result=None)

	return render_template('test.html', rows=None, result=None)

'''
Context Processor 'Injection of items'
- We can give our Flask project new variables that are accesible in HTML
- The function must return a dictionary
'''
@app.context_processor
def getYear():
	current = datetime.datetime.now()

	return dict(year=str(current.year))

# Alternative way to run via python3.
if __name__ == '__main__':
	app.run(debug=True)
