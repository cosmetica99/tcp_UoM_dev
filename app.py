# save this as app.py
from flask import Flask, render_template,jsonify
import pyodbc

app = Flask(__name__)
###Function###
def connection():
    s = 'DMK-N-900037\SQLSERVER2019' #Your server name 
    d = 'WSTCP' 
    u = 'SYSTEM_ITALI' #Your login
    p = 'SYS123' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    return conn

@app.route("/")
def getUoMFromDb():
    UoM = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM [dbo].[SapUoM]")
    for row in cursor.fetchall():
        UoM.append({"id": row[0], "material_id": row[1],"received_Unit": row[2],"amount": row[3], "To_be_unit": row[4], "Desc": row[5]})
    conn.close()

    # UoM.append(jsonify({'message': 'show all values'},{'data': UoM} ))
    return render_template("main.html", UoMData = UoM)

@app.route("/getUoM")
def getUomFromData():
    return "This session will going to check the order UoM from SAP side."


if(__name__ == "__main__"):
    app.run()