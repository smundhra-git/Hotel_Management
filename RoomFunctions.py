import os
import mysql.connector as connector
import pandas


def createroom():
    os.system('cls')
    print('*********************************************************')
    print('                 CREATE NEW ROOM')
    print('*********************************************************')
    print()
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()

    roomno = input('Enter Room No: ')
    type = input('Enter Room Type: ')
    charges = input('Enter Room Charges: ')
    status = 'Vacant'
    qry = "insert into roommaster values({},'{}',{},'{}')".format(roomno, type, charges, status)
    mycursor.execute(qry)
    con.commit()
    con.close()
    print()
    print('New Room Created Successfully !')
    print()
    input('Press Enter To Continue..........')


def showallrooms():
    os.system('cls')
    print('*********************************************************')
    print('                       ALL ROOMS')
    print('*********************************************************')
    print()
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    mycursor.execute('Select * from roommaster')
    result = mycursor.fetchall()
    df = pandas.DataFrame(result, columns=['Roomno', 'Type', 'Charges', 'Status'])
    con.close()
    print(df.to_string(index=False))
    print()
    input('Press Enter To Continue..........')
