import psycopg2

try:
    connection=psycopg2.connect(
    host='localhost', 
    user='postgres',
    password='1502Luis*',
    database='medicamentos')
    print("Conexion Exitosa")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)  
except Exception as ex:
  print(ex)