# Luchia
from backend import *

cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price": 40, "available": "True", "current_km": "0"},
    {"id": 2, "brand": "Ford", "model": "F150", "rental_price": 60, "available": "True", "current_km": "0"},
    {"id": 3, "brand": "Opel", "model": "Insignia", "rental_price": 35, "available": "True", "current_km": "0"}
    ]


def check_available_cars():
    print(f'Available cars:')
    for car in cars:
        status = 'Available' if car['available'] else 'Rented'
        print(f"{car['id']}: {car['brand']} {car['model']} - {status}")


def rent_car(_cars, car_id):
    for car in cars:
        if car["id"] == car_id:
            if car["available"]:
                car["available"] = False
                return f"You rented {car['brand']} {car['model']}."
            else:
                return "The car is already rented."
    return "Unavailable car ID."


def return_car(__cars, car_id):
    for car in cars:
        if car["id"] == car_id:
            if not car["available"]:
                car["available"] = True
                return f"You returned {car['brand']} {car['model']}."
            else:
                return "The car is already available."
    return "Unavailable car ID."


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
            car_id = int(input("Enter the car ID you want to rent: "))
            print(rent_car(cars, car_id))
        elif choice == '3':
            car_id = int(input("Enter the car ID you want to return: "))
            print(return_car(cars, car_id))
        elif choice == '4':
            admin_menu()
        elif choice == '5':
            exit('You exited the program.')
        else:
            print('Invalid option. Please try again.')
