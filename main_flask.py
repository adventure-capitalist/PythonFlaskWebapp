#!/usr/bin/env python
# accesses flak's libraries and import the one holding Flask itse;f
from flask import Flask , render_template, request
from horoscopeapi import zodiac_sign, get_horoscope

app = Flask("Test")

def calculate_gen(year_parameter) :
    gen='Unknown'

    # add logic here to identify generation
    if year_parameter >= 1964 and year_parameter <= 1978:
        gen='very OLD'
    if year_parameter >= 1979 and year_parameter <= 1995:
         gen='Y - Millenials'
    if year_parameter >= 1996 and year_parameter <= 2012:
        gen='Z'

    return gen

@app.route("/")
def default():
    m = "Welcome to my page"
    return render_template("hello.html", message=m)

@app.route("/<vistor>")
def hello(vistor):
    m = "Welcome to my page: " + vistor.title()
    return render_template("hello.html", message=m)
    #return "hello"



@app.route("/gen", methods = ["POST"])
def showgeneration():
    form_data = request.form
    year = form_data["dob"]


    gen = calculate_gen(int(year))
    return render_template("gen.html", generation = gen)

@app.route("/horosope", methods = ["POST"])
def handlehoroscope():
    form_data = request.form
    day = form_date["day"]
    month = form_date["month"]

    zsign = zodiac_sign(month, day)
    data = get_horoscope(z_sign)
    return render_template(horosope.html", data = zsi)



app.run()



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
