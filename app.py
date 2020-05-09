#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/assignments.html")
def page1():
    return render_template('assignments.html')

@app.route("/classes.html")
def page2():
    return render_template('classes.html')

#start the server
if __name__ == "__main__":
    app.run()