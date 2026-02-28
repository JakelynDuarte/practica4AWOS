from flask import Flask, render_template, request, jsonify, make_response, session
import mysql.connector

app = Flask(__name__)

@app.route('/clientes')
def clientes():
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_dam_repo4a_usr",
        password="5BYtj5fxKLs;",
        database="u760464709_dam_repo4a_bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clientes")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))
    

