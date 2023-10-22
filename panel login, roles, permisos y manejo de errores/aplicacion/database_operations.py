def insert_data(mysql, data):
    cur = mysql.connection.cursor()
    # Tu lógica para insertar datos
    cur.close()

def query_data(mysql, query):
    cur = mysql.connection.cursor()
    # Tu lógica para consultar datos
    cur.close()
