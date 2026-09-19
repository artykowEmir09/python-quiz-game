import json
import os
from datetime import datetime


FILE_NAME = "library_data.json"


# ==========================================
# DATA
# ==========================================

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            pass

    return {
        "books": {},
        "members": {}
    }


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# ==========================================
# BOOK FUNCTIONS
# ==========================================

def generate_book_id(data):

    if not data["books"]:
        return "B001"

    numbers = []

    for book_id in data["books"]:
        numbers.append(int(book_id[1:]))

    new_number = max(numbers) + 1

    return f"B{new_number:03d}"


def add_book(data):

    print("\n========== ADD BOOK ==========")

    title = input("Book title: ")
    author = input("Author: ")
    year = input("Publication year: ")

    book_id = generate_book_id(data)

    data["books"][book_id] = {
        "title": title,
        "author": author,
        "year": year,
        "available": True,
        "borrowed_by": None,
        "borrow_date": None
    }

    save_data(data)

    print("\nBook added successfully!")
    print("Book ID:", book_id)

def view_books(data):

    print("\n========== ALL BOOKS ==========")

    if not data["books"]:
        print("No books available.")
        return

    for book_id, book in data["books"].items():

        status = "Available" if book["available"] else "Borrowed"

        print("\n-----------------------------")
        print("ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Status:", status)

        if not book["available"]:
            print("Borrowed by:", book["borrowed_by"])

    print("-----------------------------")


def search_book(data):

    print("\n========== SEARCH BOOK ==========")

    search = input("Enter title or author: ").lower()

    found = False

    for book_id, book in data["books"].items():

        if (
            search in book["title"].lower()
            or search in book["author"].lower()
        ):

            status = "Available" if book["available"] else "Borrowed"

            print("\n-----------------------------")
            print("ID:", book_id)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("Status:", status)

            found = True

    if not found:
        print("No matching books found.")


def delete_book(data):

    print("\n========== DELETE BOOK ==========")

    book_id = input("Enter book ID: ").upper()

    if book_id not in data["books"]:
        print("Book not found.")
        return

    book = data["books"][book_id]

    if not book["available"]:
        print("You cannot delete a borrowed book.")
        return

    print("Book:", book["title"])

    confirm = input("Delete this book? (yes/no): ")

    if confirm.lower() == "yes":

        del data["books"][book_id]

        save_data(data)

        print("Book deleted successfully.")

    else:
        print("Deletion cancelled.")


# ==========================================
# MEMBER FUNCTIONS
# ==========================================

def generate_member_id(data):

    if not data["members"]:
        return "M001"

    numbers = []

    for member_id in data["members"]:
        numbers.append(int(member_id[1:]))

    new_number = max(numbers) + 1

    return f"M{new_number:03d}"


def add_member(data):

    print("\n========== ADD MEMBER ==========")

    name = input("Member name: ")
    phone = input("Phone number: ")

    member_id = generate_member_id(data)

    data["members"][member_id] = {
        "name": name,
        "phone": phone,
        "borrowed_books": []
    }

    save_data(data)

    print("\nMember added successfully!")
    print("Member ID:", member_id)


def view_members(data):

    print("\n========== ALL MEMBERS ==========")

    if not data["members"]:
        print("No members found.")
        return

    for member_id, member in data["members"].items():

        print("\n-----------------------------")
        print("ID:", member_id)
        print("Name:", member["name"])
        print("Phone:", member["phone"])

        if member["borrowed_books"]:
            print("Borrowed books:")

            for book_id in member["borrowed_books"]:
                print(" -", book_id)

        else: