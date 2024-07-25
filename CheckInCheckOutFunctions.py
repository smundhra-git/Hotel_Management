import os
import mysql.connector as connector
import pandas


def printheading():
    os.system('cls')
    print('*********************************************************')
    print('                       CHECK-IN')
    print('*********************************************************')
    print()


def showavailablerooms(roomtype):
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    qry = "select * from roommaster where status = 'Vacant' and roomtype = '{}'".format(roomtype)
    mycursor.execute(qry)
    df = pandas.DataFrame(mycursor.fetchall(), columns=['RoomNo', 'RoomType', 'Charges', 'Status'])
    print()
    print(df.to_string(index=False))
    print()


def checkin():
    os.system('cls')
    printheading()
    print('Enter Your Choice For Room Types: ')
    print('1. AC')
    print('2. NON AC')
    print('3. SUPER DELUXE')
    print('4. Exit')
    print()

    roomchoice = int(input('Enter Your Choice: '))
    roomtype = ''

    if roomchoice == 1:
        roomtype = 'AC'
    elif roomchoice == 2:
        roomtype = 'NON AC'
    elif roomchoice == 3:
        roomtype = 'SUPER DELUXE'
    elif roomchoice == 4:
        return

    showavailablerooms(roomtype)

    roomno = input('Enter Room No From The List Given Above To Be booked: ')

    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    qry = 'select curdate()'
    mycursor.execute(qry)
    currentdate = mycursor.fetchall()
    checkindate = currentdate[0][0]

    print('Check-In Date: ', checkindate)
    custname = input('Enter Customer Name: ')
    phone = input('Enter Customer Phone No: ')

    q = "insert into checkin values({},'{}','{}','{}','Occupied')".format(roomno, custname, phone, checkindate)
    mycursor.execute(q)
    q = "update roommaster set status = 'Occupied' where roomno = {}".format(roomno)
    mycursor.execute(q)
    con.commit()
    print()
    print('Room Booked !')
    print()
    input('Press Enter To Continue........')
    # ************************************************


def getroomcharges(roomno):
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    q = "select charges from roommaster where roomno = {}".format(roomno)
    mycursor.execute(q)
    roomno = mycursor.fetchall()
    return int(roomno[0][0])


def getdays(roomno):
    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()
    q = "select datediff(curdate(),checkindate) from checkin where roomno = {}".format(roomno)
    mycursor.execute(q)
    days = mycursor.fetchall()
    return int(days[0][0])


def checkout():
    os.system('cls')
    print('*********************************************************')
    print('                       CHECK-OUT')
    print('*********************************************************')
    print()

    con = connector.connect(host="localhost", user="root", passwd="root", database="Hotel")
    mycursor = con.cursor()

    roomno = input('Enter Room No For Checking Out: ')
    q = "select * from checkin where roomno = {} and status = 'Occupied'".format(roomno)
    charges = getroomcharges(roomno)
    mycursor.execute(q)
    roomdata = mycursor.fetchall()
    if mycursor.rowcount > 0:
        df = pandas.DataFrame(roomdata, columns=['Roomno', 'Customername', 'Phone', 'Checkindate', 'Status'])
        print()
        print(df.to_string(index=False))
        print()
        print('Room Charges: ', charges)
        days = getdays(roomno)
        if days == 0:
            days += 1
        print('Days Stayed: ', days)
        amount = charges * days
        print('Amount To Be Paid: ', amount)
        print()

        qry = 'select curdate()'
        mycursor.execute(qry)
        currentdate = mycursor.fetchall()
        checkoutdate = currentdate[0][0]

        custname = df.at[0, 'Customername']
        checkindate = df.at[0, 'Checkindate']

        print('Room No: ', roomno)
        print('Customer Name: ', custname)
        print('Check-In Date: ', checkindate)
        print('Check-Out Date: ', checkoutdate)
        print('No Of Days: ', days)
        print('Room Charges: ', charges)
        print('Total Amount: ', amount)

        confirm = input('Confirm Checkout (y / n): ')
        if confirm == 'y':
            q = "update checkin set status = 'Vacant' where roomno = {}".format(roomno)
            mycursor.execute(q)
            q = "update roommaster set status = 'Vacant' where roomno = {}".format(roomno)
            mycursor.execute(q)
            q = "insert into checkout values({},'{}','{}','{}', {}, {}, {})"
            q = q.format(roomno, custname, checkindate, checkoutdate, days, charges, amount)
            mycursor.execute(q)
            con.commit()
            print()
            print('Check-Out Successful !')
    else:
        print('No Booking For This RoomNo !')

    print()
    input('Press Enter To Continue........')
