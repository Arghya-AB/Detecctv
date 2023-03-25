from flask import Flask
import sqlite3
con = sqlite3.connect("al.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE if not exists Alerts(longitude, latitude, time, type)")

app = Flask(__name__)

from flask import request

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(f"Insert into Alerts values({request.form['longitude']}, {request.form['latitude']}, '{request.form['time']}', '{request.form['type']}')")
        cur.execute(f"Insert into Alerts values({request.form['longitude']}, {request.form['latitude']}, '{request.form['time']}', '{request.form['type']}')")
        return "Accepted"
    else:
        return open("file.html").read()

@app.route('/alerts', methods=['GET', 'POST'])
def alert():
    alerts_list = []
    res = cur.execute("Select * from Alerts")
    for i in res.fetchall():
        json = {"longitude": i[0], "latitude": i[1], "time": i[2], "type": i[3]}
        alerts_list.append(json)
    return alerts_list