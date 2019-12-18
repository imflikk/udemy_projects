#!/usr/bin/python3

######
# Basic website using Python flask
#
# Additional files used with this script:
#   -'templates' folder (holds html files)
#   -'static' folder (holds css and image files)
#   -Files needed for deploying on Heroku
#       *requirements.txt(with necessary Python libraries)
#       *Procfile (with information on running the app.  i.e. 'web: gunicorn website:app')
#       *runtime.txt (version of Python to use)
######

from flask import Flask, render_template

# Create Flask app variable
app = Flask(__name__)

# Create decorator and function for the home page.  Load 'home.html' file as the template
@app.route('/')
def home():
    return render_template("home.html")

# Create decorator and function for the about page.  Load 'about.html' file as the template
@app.route('/about/')
def about():
    return render_template("about.html")

# If this specific script is run directly (rather than called from another script), run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
