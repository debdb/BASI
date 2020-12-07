from datetime import datetime
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/gestoreHome')
def gestoreHome():
    return render_template(
        "gestoreHome.html",
        title = "gestoreHome",
        content = "gestoreHome")



@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')

@app.route('/gestoreAddMovie')
def gestoreAddMovie():
    return render_template(
        "gestoreAddMovie.html",
        title = "gestoreAddMovie",
        content = "gestoreAddMovie")

@app.route('/gestoreAnalytics')
def gestoreAnalytics():
    return render_template(
        "gestoreAnalytics.html",
        title = "gestoreAnalytics",
        content = "gestoreAnalytics")


@app.route('/gestoreUser')
def gestoreUser():
    return render_template(
        "gestoreUser.html",
        title = "gestoreUser",
        content = "gestoreUser")

