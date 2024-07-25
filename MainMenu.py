import os
import RoomFunctions
import CheckInCheckOutFunctions
import DataAnalysis

while True:
    os.system('cls')
    print('*********************************************************')
    print('                HOTEL RESERVATION SYSTEM')
    print('*********************************************************')
    print()
    print('1. Create New Room')
    print('2. Show All Rooms')
    print('3. Check-In')
    print('4. Check-Out')
    print('5. Data Analysis')
    print('0. Exit')
    print()
    choice = int(input('Enter your choice: '))

    if choice == 0:
        break
    elif choice == 1:
        RoomFunctions.createroom()
    elif choice == 2:
        RoomFunctions.showallrooms()
    elif choice == 3:
        CheckInCheckOutFunctions.checkin()
    elif choice == 4:
        CheckInCheckOutFunctions.checkout()
    elif choice == 5:
        DataAnalysis.showchartmenu()











