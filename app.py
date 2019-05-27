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
import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

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
