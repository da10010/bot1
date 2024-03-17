import mysql.connector

conn = mysql.connector.connect(
    host= '173.211.81.11',  
    user= 'ljywsbcn_admin',
    password= '#desenvolvendo2024',
    database= 'ljywsbcn_bot_atendimento')
cursor = conn.cursor() 


def insert(phone, status, dateContact, nameUser):
                cursor.execute("INSERT INTO usuario (userPhone,status,dateContact, nameUser) VALUES ('{}', '{}', '{}','{}')".format(phone, status, dateContact, nameUser))
                conn.commit()


# insert(000000, 5, "12-0-20224", "joao")
                
def dateUser(phone):
    query = "SELECT dateContact FROM usuario WHERE userPhone = '{}'".format(phone)
    cursor.execute(query)
    resultCursor = cursor.fetchone()
    return resultCursor


def delete():
        query = "DELETE FROM usuario WHERE userPhone = '+55 47 9978-8171'"
        cursor.execute(query)
        conn.commit()


def userName(nameUser, phone):
               cursor.execute("UPDATE usuario SET nameUser = '{}' WHERE userPhone = '{}'".format(nameUser, phone))
               conn.commit()

def search_name(phone):
            query = "SELECT nameUser FROM usuario WHERE userPhone = '{}' ".format(phone)
            cursor.execute(query)
            resultSearch =  cursor.fetchone()
            return resultSearch[0]

delete()

#print(search_name('+55 75 8805-6052'))
        