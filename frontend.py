# Luchia
from backend import *

admin_pass = 'admin123'


def check_available_cars():
    print(f'Available cars:')
    for car in cars:
        status = 'Available' if car['available'] else 'Rented'
        print(f"{car['id']}: {car['brand']} {car['model']} - {status}")


def display_menu():
    print("\nWelcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Administrator")
    print("5. Exit")
    return input("Please choose an option (1-5): ")


def admin_menu():
    print("\nWelcome to RentACar admin console!")
    print("1. Add Car")
    print("2. Delete Car")
    print("3. Return to main menu")
    return input("Please choose an option (1-3): ")


def main_menu():
    while True:
        choice = display_menu()

        if choice == '1':
            check_available_cars()
        elif choice == '2':
            car_id = int(input('Enter the car ID you want to rent: '))
            print(rent_car(cars, car_id))
        elif choice == '3':
            car_id = int(input('Enter the car ID you want to return: '))
            print(return_car(cars, car_id))
        elif choice == '4':
            print('Enter the admin password:')
            password = input()
            if password == admin_pass:
                command = admin_menu()
                if command == '1':
                    add_car()
                elif command == '2':
                    remove_car()
                elif command == '3':
                    main_menu()
            else:
                print('Incorrect password, access denied.\nReturning to main menu.')
                main_menu()
        elif choice == '5':
            exit('You exited the program.')
        else:
            print('Invalid option. Please try again.')

