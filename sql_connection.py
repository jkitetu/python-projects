import pymysql

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:

        __cnx = pymysql.connect(user='root', password='Toughees@1',
                      host='127.0.0.1',
                      database='grocerystore')
    return __cnx