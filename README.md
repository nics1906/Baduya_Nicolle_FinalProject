# Project Overview

This Python Application serves as a complete Car Rental Management System. I prefer the system to be organized, reliable, and easy to use for managing cars and rental transactions. This CLI-based application follows a modular design and Object-Oriented Programming (OOP) principles with clean separation of data, logic, and user interface.

Users can easily add unlimited cars, rent available vehicles, return rented cars, view all rental records, and keep all data safe. The system automatically saves all data to a JSON file and never crashes due to invalid input.

# KEY FEATURES OF THE CLI-based Car Rental Management System

* Add new cars
* View all cars with availability status
* Rent available cars
* Return rented cars
* View all rental records
* Auto-calculate rental fees
* Data persistence: Auto-save / auto-load from JSON
* Full error handling (never crashes on invalid input)

# Error Handling

Built-in protection ensures the app never crashes:

* Empty input → Clear message
* Duplicate car IDs / plate numbers → Blocked
* Invalid menu choices → Guided correction
* Corrupted/missing JSON → Auto-reset safely
* Wrong data type → Rejected with instruction

# Advanced Python Concepts Used

1. List Comprehension – Filter/search data in one line
2. Context Manager – Safe file handling using `with open()`
3. @classmethod – Create objects from saved JSON
4. Magic/Dunder Methods – `__str__`, `__eq__` for clean object behavior
5. Type Hints – Clear data types for readability & error prevention
6. Error Handling (`try...except`) – Handles missing files, corrupted data, invalid input

# Installation & How to Run

## 1. Requirements

* Python 3.7 or higher
* No external packages needed (uses only built-in modules)

## 2. Run the App

* Open terminal / command prompt
* Navigate to the project folder

## 3. System Functions

* Add Car: Register new rental vehicles
* View Cars: See all cars and their availability
* Rent Car: Rent available vehicles to customers
* Return Car: Return rented vehicles and update status
* View Rentals: Check all rental transactions
* Save & Exit: Saves everything automatically

# Author

STUDENT: NICOLLE B. BADUYA
Section: BSCS 1B
Instructor: ALLAN IBO JR.
Course: INTERMEDIATE PROGRAMMING (Final Project)

FINAL PROJECT
Car Rental Management System
