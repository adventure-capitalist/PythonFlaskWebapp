# accesses flak's libraries and import the one holding Flask itse;f
from flask import Flask
#defines the app as a function called Flask using arguments called "my app"
app = Flask("MyApp")
#decorator that talks to the server and flask
@app.route("/<visitor>")
#defines a function called hello using arguments visitor
def hello(visitor):
    #defines variable m string + visitor variable's title
    m = "Welcome to my page:" + visitor.title()
#return's the result of a new function using the index file and variable m
    return render_template("index.html", message=m)
#decorator talks to the server and flask
@app.route("/welcome")
#defines a new function called welcome
def welcome():
#returns a string
    return "Hello welcome to my page"
#runs the flask function and debugs it
app.run(debug=True)




# from flask import Flask
#
# app = Flask("MyApp")
#
# @app.route("/<visitor>")
# def hello(visitor):
#     m = "Welcome to my page:" + vistor.title()
#     return render_template("index.html", message=m)
#     #return "Hello World"
# @app.route("/welcome")
# def welcome():
#     return "Hello welcome to my page"
#
# app.run(debug=True)
