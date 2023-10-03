from flask import Flask
### WSGI Application
app=Flask(__name__)
@app.route('/')
def welcome():
    return "welcome to my first program"


@app.route('/members')
def members():
    return " my journey starts here"

if __name__=='__main__':
    app.run(debug=True) 

