# mrparkonline
# Flask App Test
# initiative project

''' To Run:
1. python3 -m flask run
2. export FLASK_APP=filename.py --> flask run
'''

# import lines
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'

# Alternative way to run via python3.
if __name__ == '__main__':
	app.run(debug=True)
