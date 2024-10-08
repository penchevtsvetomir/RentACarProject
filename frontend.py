# Luchia
from backend import *


def check_available_cars():
    pass


def rent_car():
    pass


def return_car():
    pass


def display_menu():
    print("Welcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Administrator")
    print("5. Exit")
    return input("Please choose an option (1-5): ")


def admin_menu():
    print("Welcome to RentACar admin console!")
    print("1. Add Car")
    print("2. Delete Car")
    print("3. Return to main menu")
    return input("Please choose an option (1-3): ")


def main():
    while True:
        choice = display_menu()

        if choice == '1':
            check_available_cars()
        if choice == '2':
            rent_car()
        if choice == '3':
            return_car()
        if choice == '4':
            admin_menu()
        if choice == '5':
            exit('You exited the program.')
        else:
            print('Invalid option. Please try again:')

