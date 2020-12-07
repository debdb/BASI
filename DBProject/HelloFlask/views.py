from datetime import datetime
from flask import render_template
from HelloFlask import app
#from flask_mysqldb import MySQL


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

#mysql = MySQL(app)

#mysql.init_app(app)
#cursor = mysql.get_db().cursor()





if __name__ == '__main__':
    app.run()

@app.route('/')
@app.route('/gestoreHome')
def gestoreHome():
    return render_template(
        "gestoreHome.html",
        title = "gestoreHome" )



@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')


@app.route('/gestoreAddMovie', methods=['POST'])
def gestoreAddMovie():
    if request.method == "POST":
        details = request.form
        title = details['title']
        year = details['year']
        price = details['price']
        genre = details['genre']
        duration = details['duration']
        cast = details['cast']
        description = details['description']
        monday = details['monday']
        hourmonday = details['hourmonday']
        tuesday = details['tuesday']
        hourtuesday = details['hourtuesday']
        wednesday = details['wednesday']
        hourwednesday = details['hourwednesday']
        thusday = details['thusday']
        hourthusday = details['hourthusday']
        friday = details['friday']
        hourfriday = details['hourfriday']
        saturday = details['saturday']
        hoursaturday = details['hoursaturday']
        sunday = details['sunday']
        hoursunday = details['hoursunday']
        coverphoto = details['coverphoto']
        available = details['available']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Movies(title, year, price, genre, duration, cast, description, monday, hourmonday, tuesday, hourtuesday, wednesday, hourwednesday, thusday, hourthuesday, friday, hourfriday, saturday, hoursaturday, sunday, hoursunday, coverphoto, available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s)", (title, year, price, genre, duration, cast, description, monday, hourmonday, tuesday, hourtuesday, wednesday, hourwednesday, thusday, hourthuesday, friday, hourfriday, saturday, hoursaturday, sunday, hoursunday, coverphoto, available))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template(
        "gestoreAddMovie.html",
        title = "gestoreAddMovie")



@app.route('/gestoreAnalytics')
def gestoreAnalytics():
    return render_template(
        "gestoreAnalytics.html",
        title = "gestoreAnalytics")


@app.route('/gestoreUser')
def gestoreUser():
    return render_template(
        "gestoreUser.html",
        title = "gestoreUser")

