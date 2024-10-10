# Denis
from frontend import *
import time


def initialize_cars():
    """Creates initial database of cars."""
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Camry", "rental_price_per_km": 0.20, "mileage": 50000,
         "available": True},
        {"id": 2, "brand": "Honda", "model": "Civic", "rental_price_per_km": 0.18, "mileage": 62000, "available": True},
        {"id": 3, "brand": "Ford", "model": "Mustang", "rental_price_per_km": 0.30, "mileage": 45000,
         "available": True},
        {"id": 4, "brand": "Chevrolet", "model": "Malibu", "rental_price_per_km": 0.22, "mileage": 54000,
         "available": True},
        {"id": 5, "brand": "BMW", "model": "3 Series", "rental_price_per_km": 0.28, "mileage": 72000,
         "available": False},
        {"id": 6, "brand": "Mercedes", "model": "C-Class", "rental_price_per_km": 0.32, "mileage": 33000,
         "available": True},
        {"id": 7, "brand": "Audi", "model": "A4", "rental_price_per_km": 0.30, "mileage": 61000, "available": False},
        {"id": 8, "brand": "Nissan", "model": "Altima", "rental_price_per_km": 0.16, "mileage": 67000,
         "available": True},
        {"id": 9, "brand": "Hyundai", "model": "Elantra", "rental_price_per_km": 0.15, "mileage": 58000,
         "available": True},
        {"id": 10, "brand": "Kia", "model": "Optima", "rental_price_per_km": 0.17, "mileage": 55000, "available": True},
        {"id": 11, "brand": "Tesla", "model": "Model 3", "rental_price_per_km": 0.35, "mileage": 40000,
         "available": False},
        {"id": 12, "brand": "Volkswagen", "model": "Passat", "rental_price_per_km": 0.23, "mileage": 49000,
         "available": True},
        {"id": 13, "brand": "Mazda", "model": "Mazda3", "rental_price_per_km": 0.18, "mileage": 51000,
         "available": True},
        {"id": 14, "brand": "Subaru", "model": "Impreza", "rental_price_per_km": 0.19, "mileage": 47000,
         "available": True},
        {"id": 15, "brand": "Lexus", "model": "ES", "rental_price_per_km": 0.29, "mileage": 61000, "available": True},
    ]
    return cars


def add_car():
    car_id = int(input("Enter a car ID: "))
    car_brand = input("Enter brand name: ")
    car_model = input("Enter model name: ")
    car_rental_price = float(input("Enter rental price ($/km): "))
    car_mileage = int(input("Enter mileage: "))

    new_car = {
        "id": car_id,
        "brand": car_brand,
        "model": car_model,
        "rental_price_per_km": car_rental_price,
        "mileage": car_mileage,
        "available": True
    }

    cars.append(new_car)

    return f"Car added successfully. Returning to main menu..."


def remove_car():
    car_id = int(input("Enter a car ID: "))

    for car in cars:
        if car["id"] == car_id:
            cars.remove(car)
            return "Car removed successfully."
    return "Car ID not found. Returning to main menu..."


def edit_car():
    car_id = int(input("Enter a car ID: "))

    # Finding the car to edit
    car = next((car for car in cars if car["id"] == car_id), None)
    if not car:
        print("Car ID not found. Returning to main menu...")
        time.sleep(3)
        return

    key = input("Enter property to edit (brand, model, price per km, mileage): ").strip()

    # Check if the provided key is valid
    if key in car:
        if isinstance(car[key], (int, float)):
            new_value = input(f"Enter new value for {key} (current: {car[key]}): ")
            # Validate if the input is a number for numerical properties
            try:
                car[key] = float(new_value) if '.' in new_value else int(new_value)
            except ValueError:
                print("Invalid input! The value must be a number.")
                time.sleep(3)
                return
        else:
            new_value = input(f"Enter new value for {key} (current: {car[key]}): ")
            car[key] = new_value
        print("Car property updated successfully. Returning to main menu...")
    else:
        print("Invalid property name. Returning to main menu...")

    time.sleep(3)  # Adding a sleep after the edit operation


def rent_car(cars, car_id):
    """Processes a customer request to rent a car."""
    for car in cars:
        if car["id"] == car_id and car["available"]:
            car["available"] = False
            return f"You have successfully rented the {car['brand']} {car['model']}. Enjoy the ride!"
    return "Car is unavailable or invalid car ID! Returning to main menu..."


def return_car(cars, car_model):
    """"Processes a customer request to return a rented car."""
    for car in cars:
        if car_model == car["brand"] + " " + car["model"] and car["available"] == False:
            car["available"] = True
            return "You successfully returned the car!"
    return "No such car found! Please try again."

def calculate_total(car_model, mileage, cars):
    """Calculates the total rented car price."""
    for car in cars:
        if car_model == car["brand"] + " " + car["model"]:
            if mileage < car["mileage"]:
                return "Error! New mileage cannot be less than the car's original mileage."
            total = car["rental_price_per_km"] * (mileage - car["mileage"])
            car["mileage"] = mileage
            return f"Your total is: ${total:.2f} USD."


