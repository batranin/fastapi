from multiprocessing import connection
import pymysql.cursors 

def connectdb():
    # Подключиться к базе данных.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',                             
                             db='goods',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor) 
    print ("connect successful!!") 
    return connection
# Вспомогательная функция для упрощения получения результатов по ключу
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d

def select_items(barcode):
    connection = connectdb()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `goodsbarcodes` WHERE `barcode`=%s"
            cursor.execute(sql, (barcode,))
            result = cursor.fetchone()
            print(result)
    except connection.Error as error:
        print("Error connection to database", error)
    finally:
        if connection: connection.close()

    return   result
