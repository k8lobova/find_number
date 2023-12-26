from find import find
from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/',methods = ['POST'])
def findnumber():
    global text
    text = request.form['text']
    found = find(text)
    return render_template('index.html',found=found)



if __name__ == "__main__":
     app.run(debug=True)