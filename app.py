from flask import Flask, render_template, request, jsonify, make_response, session
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

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

@app.post('/cliente')
def cliente():
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_dam_repo4a_usr",
        password="5BYtj5fxKLs;",
        database="u760464709_dam_repo4a_bd"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO clientes (idCliente, nombreCliente, numero) VALUES (%s, %s, %s)"
    val = (
        request.form['txtCliente'],
        request.form['cboNombreCliente'],
        request.form['txtnumero']
    )
    mycursor.execute(sql, val)
    mydb.commit()
    return "correcto"

@app.put('/cliente')
def actualizar_cliente():
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_dam_repo4a_usr",
        password="5BYtj5fxKLs;",
        database="u760464709_dam_repo4a_bd"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE clientes SET nombreCliente = %s, numero = %s WHERE idCliente = %s"
    val = (
        request.form['cboNombreCliente'],
        request.form['txtnumero'],
        request.form['txtCliente']
    )
    mycursor.execute(sql, val)
    mydb.commit()
    return "actualizado"

@app.delete('/cliente/<id>')
def eliminar_cliente(id):
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_dam_repo4a_usr",
        password="5BYtj5fxKLs;",
        database="u760464709_dam_repo4a_bd"
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM clientes WHERE idCliente = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return "eliminado"
