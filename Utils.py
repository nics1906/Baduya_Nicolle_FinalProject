"""
utils.py
Helper functions for CLI interface
"""

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def get_input(prompt):
    return input(prompt)


def get_int_input(prompt):
    """Safe integer input handling"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")