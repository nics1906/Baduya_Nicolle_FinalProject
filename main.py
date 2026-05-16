"""
CLI Car Rental System
A command-line application for managing car rentals
"""

import json
import os

DATA_FILE = "car_rental.json"


# ------------------------------ DATA ------------------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "cars": [],
            "rentals": []
        }

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ------------------------------ HELPER ------------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def get_input(prompt):
    return input(prompt)


# ------------------------------ MAIN MENU ------------------------------
def main_menu():
    while True:
        clear()

        print("=" * 40)
        print("🚗 CAR RENTAL SYSTEM".center(40))
        print("=" * 40)
        print("1. Add Car")
        print("2. View Cars")
        print("3. Rent Car")
        print("4. Return Car")
        print("5. View Rentals")
        print("6. Exit")
        print("-" * 40)

        choice = get_input("Enter choice: ")

        if choice == "1":
            add_car()
        elif choice == "2":
            view_cars()
        elif choice == "3":
            rent_car()
        elif choice == "4":
            return_car()
        elif choice == "5":
            view_rentals()
        elif choice == "6":
            print("\n🚗 Thank you for using Car Rental System!")
            break


# ------------------------------ ADD CAR ------------------------------
def add_car():
    data = load_data()

    model = get_input("Enter car model: ")
    plate = get_input("Enter plate number: ")

    car = {
        "model": model,
        "plate": plate,
        "available": True
    }

    data["cars"].append(car)
    save_data(data)

    print("\n✅ Car added successfully!")
    pause()


# ------------------------------ VIEW CARS ------------------------------
def view_cars():
    data = load_data()

    if not data["cars"]:
        print("\nNo cars available!")
        pause()
        return

    print("\n🚗 AVAILABLE CARS")

    for i, car in enumerate(data["cars"], 1):
        status = "Available" if car["available"] else "Rented"
        print(f"{i}. {car['model']} | Plate: {car['plate']} | {status}")

    pause()


# ------------------------------ RENT CAR ------------------------------
def rent_car():
    data = load_data()

    available_cars = [c for c in data["cars"] if c["available"]]

    if not available_cars:
        print("\n❌ No available cars!")
        pause()
        return

    print("\n🚗 AVAILABLE FOR RENT:")
    for i, car in enumerate(available_cars, 1):
        print(f"{i}. {car['model']} ({car['plate']})")

    choice = int(get_input("\nSelect car number: ")) - 1

    if 0 <= choice < len(available_cars):
        name = get_input("Enter your name: ")
        days = int(get_input("How many days: "))

        car = available_cars[choice]
        car["available"] = False

        rental = {
            "name": name,
            "car": car["model"],
            "plate": car["plate"],
            "days": days
        }

        data["rentals"].append(rental)
        save_data(data)

        print("\n✅ Car rented successfully!")

    else:
        print("❌ Invalid choice!")

    pause()


# ------------------------------ RETURN CAR ------------------------------
def return_car():
    data = load_data()

    plate = get_input("Enter plate number to return: ")

    found = False

    for car in data["cars"]:
        if car["plate"] == plate:
            car["available"] = True
            found = True

    if found:
        save_data(data)
        print("\n✅ Car returned successfully!")
    else:
        print("\n❌ Car not found!")

    pause()


# ------------------------------ VIEW RENTALS ------------------------------
def view_rentals():
    data = load_data()

    if not data["rentals"]:
        print("\nNo rentals yet!")
        pause()
        return

    print("\n📄 RENTAL RECORDS")

    for r in data["rentals"]:
        print(f"👤 {r['name']} rented {r['car']} for {r['days']} days")

    pause()


# ------------------------------ RUN ------------------------------
if __name__ == "__main__":
    main_menu()