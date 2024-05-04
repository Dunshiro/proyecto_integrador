import mysql.connector

try:
    cnx = mysql.connector.connect(
        user='root',
        password='mysql',
        host='localhost',
        database='proyecto_integrador'
    )

    if cnx.is_connected():
        print("Conexión exitosa a la base de datos")
    else:
        print("La conexión no está activa")

    cnx.close()

except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")