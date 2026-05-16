"""
models.py
Contains OOP classes for the Car Rental System
"""

import json
import os


DATA_FILE = "car_rental.json"


class Car:
    """Represents a single car in the system"""

    def __init__(self, model, plate, available=True):
        self.model = model
        self.plate = plate
        self.available = available

    def to_dict(self):
        return {
            "model": self.model,
            "plate": self.plate,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Car(data["model"], data["plate"], data["available"])


class Rental:
    """Represents a rental transaction"""

    def __init__(self, name, car_model, plate, days):
        self.name = name
        self.car_model = car_model
        self.plate = plate
        self.days = days

    def to_dict(self):
        return {
            "name": self.name,
            "car": self.car_model,
            "plate": self.plate,
            "days": self.days
        }

    @staticmethod
    def from_dict(data):
        return Rental(
            data["name"],
            data["car"],
            data["plate"],
            data["days"]
        )


class CarRentalSystem:
    """Main system handling cars and rentals"""

    def __init__(self):
        self.data = self.load_data()

    # ---------------- FILE HANDLING ----------------
    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return {"cars": [], "rentals": []}

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.data, file, indent=4)

    # ---------------- CAR FUNCTIONS ----------------
    def add_car(self, car: Car):
        self.data["cars"].append(car.to_dict())
        self.save_data()

    def get_cars(self):
        return self.data["cars"]

    def get_available_cars(self):
        return [c for c in self.data["cars"] if c["available"]]

    def rent_car(self, index, name, days):
        available = self.get_available_cars()

        if index < 0 or index >= len(available):
            return False

        car = available[index]
        car["available"] = False

        rental = Rental(name, car["model"], car["plate"], days)
        self.data["rentals"].append(rental.to_dict())

        self.save_data()
        return True

    def return_car(self, plate):
        for car in self.data["cars"]:
            if car["plate"] == plate:
                car["available"] = True
                self.save_data()
                return True
        return False

    def get_rentals(self):
        return self.data["rentals"]