import mysql.connector
import json

def update_user(username, ip_address, foundation_number, date):
    DB_config = json.loads(open('config.json').read())
    mycursor = mysql.connector.cursors.DictCursor(DB_config)
    myquery = "UPDATE empform SET IPAdress=%s, FoundationNumber=%s, Date=%s WHERE Username=%s"
    values = (ip_address, foundation_number, date, username)
    mycursor.execute(myquery, values)
    conn = mysql.connector.connect(host=DB_config['host'], user=DB_config['user'], password=DB_config['password'], database=DB_config['database'])
    if mycursor.lastrowid > 0:
        print("Record updated successfully")
    else: print("Error updating record")
    conn.close()

update_user("Username1", "IPAdress", "FoundationNumber", "Date")