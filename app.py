#flask tutorial and, variable rules, building urls dyanmically
from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/')
def welcome():
    return "Dhanush Babu's tutorial"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed with a score of " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed with a score "+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks>50:
        result ='success'
    else:
        result ='fail'
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug = True)