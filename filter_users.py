import json
import os

def load_users():
    """Load and return user data from users.json."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    users_file = os.path.join(base_dir, "users.json")

    with open(users_file, "r", encoding="utf-8") as file:
        return json.load(file)


def filter_users_by_name(name):
    """Print users whose name matches the provided name input."""
    users = load_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(min_age, max_age):
    """Print users whose age matches the provided age range input."""
    users = load_users()
    filtered_users = [user for user in users if min_age <= user["age"] <= max_age]

    for user in filtered_users:
        print(user)


def filter_by_email(email):
    """Print users whose email matches the provided email input."""
    users = load_users()
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("Would you like to filter by name, age, or email: ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        min_age = int(input("Enter minimum age: ").strip())
        max_age = int(input("Enter maximum age: ").strip())
        filter_by_age(min_age, max_age)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
