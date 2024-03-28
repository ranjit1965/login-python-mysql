import mysql.connector

def insert_employee_data(username, ip_address, foundation_number, date):
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password',
        database = 'empdb'
    )
    cursor = db.cursor()
    query = "INSERT INTO empform VALUES(%s, %s, %s, %s)"
    values = (username, ip_address, foundation_number, date)
    inserted_data = cursor.execute(query, values)
    
    if inserted_data:
        print("Insertion successful!")
    else:
        print("Insertion failed.")
    db.close()