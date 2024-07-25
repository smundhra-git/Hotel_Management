import mysql.connector as connector
import os
import pandas
import matplotlib.pyplot as plt


def shownooftimesroombookedchart():
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    q = "select roomno,count(*) 'times' from checkin group by roomno"
    mycursor.execute(q)
    data = mycursor.fetchall()
    df = pandas.DataFrame(data, columns=['roomno', 'times'])
    x = list(df['roomno'])
    y = list(df['times'])
    plt.bar(x,y)
    plt.xticks(x)
    plt.yticks(y)
    plt.title('Room No and No Of Times It Is Booked')
    plt.xlabel('ROOM NO')
    plt.ylabel('BOOKED NO OF TIMES')
    plt.show()

def showroomnoandchargeschart():
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    q = "select roomno,charges from roommaster"
    mycursor.execute(q)
    data = mycursor.fetchall()
    df = pandas.DataFrame(data, columns=['roomno', 'charges'])
    x = list(df['roomno'])
    y = list(df['charges'])
    plt.plot(x,y)
    plt.xticks(x)
    plt.yticks(y)
    plt.title('Room No and Charges')
    plt.xlabel('ROOM NO')
    plt.ylabel('CHARGES')
    plt.show()

def showroomwisetotalamountchart():
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    q = "select roomno, sum(totalcharges) from checkout group by roomno"
    mycursor.execute(q)
    data = mycursor.fetchall()
    df = pandas.DataFrame(data, columns=['roomno', 'amount'])
    x = list(df['roomno'])
    y = list(df['amount'])
    plt.pie(y,labels=x,shadow=True)
    plt.title('ROOM NO AND AMOUNT RECEIVED CHART')
    plt.show()

def showchartmenu():
    while True:
        os.system('cls')
        print('*********************************************************')
        print('                       DATA ANALYSIS')
        print('*********************************************************')
        print()
        print('1. Show Room No and No Of Times It Is Booked Chart')
        print('2. Show Room No and Charges Chart')
        print('3. Show Room No and Amount Received Chart')
        print('0. Exit')
        print()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            break
        if choice == 1:
            shownooftimesroombookedchart()
        if choice == 2:
            showroomnoandchargeschart()
        if choice==3:
            showroomwisetotalamountchart()