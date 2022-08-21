from flask import Flask, render_template ## used to import flask module

app = Flask(__name__) ## creates flask obj

@app.route('/') ## sets the app route. url location for http
def hello_internet():
    return render_template('index.html') ## this will be returned and displayed in browser

if __name__=='__main__': ## this code is to run the app
    app.run(debug=True, host='0.0.0.0', port=5000)