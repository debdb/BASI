from datetime import datetime
from flask import render_template
from HelloFlask import app
from flask import Flask,render_template, request
#from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cinema'
 
mysql = MySQL(app)

#Creating a connection cursor
cursor = mysql.connection.cursor()
 
#Executing SQL Statements
#cursor.execute(CREATE TABLE table_name(field1, field2))
cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
#Saving the Actions performed on the DB
mysql.connection.commit()



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
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Movies(title, year, price, genre, duration, cast, description, monday, hourmonday, tuesday, hourtuesday, wednesday, hourwednesday, thusday, hourthuesday, friday, hourfriday, saturday, hoursaturday, sunday, hoursunday, coverphoto, available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s)", (title, year, price, genre, duration, cast, description, monday, hourmonday, tuesday, hourtuesday, wednesday, hourwednesday, thusday, hourthuesday, friday, hourfriday, saturday, hoursaturday, sunday, hoursunday, coverphoto, available))
        mysql.connection.commit()
        cursor.close()
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

