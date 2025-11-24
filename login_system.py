# import json
# import os

# DATA_FILE = "users.json"

# # Load users from file or create default users
# def load_users():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as f:
#             return json.load(f)
#     else:
#         # Default users
#         users = {
#             "dhananjay": "1234",
#             "shubham": "1111",
#             "ganesh": "2222",
#             "rohit": "3333",
#             "suresh": "4444",
#             "raj": "5555",
#             "neha": "6666",
#             "priya": "7777",
#             "sham": "8888",
#             "ram": "9999",
#             "akash": "0000"
#         }
#         save_users(users)
#         return users

# # Save users to file
# def save_users(users):
#     with open(DATA_FILE, "w") as f:
#         json.dump(users, f)

# users = load_users()

# # Main login loop
# while True:
#     username = input("\nEnter username: ").upper()
#     password = input("Enter password: ").upper()

#     # If username exists
#     if username in users:
#         # If password correct
#         if users[username] == password:
#             print(f"\n✅ Welcome {username} sir ")
#         else:
#             print("\n❌ Wrong password. You have 2 more chances.")

#             chances = 2
#             while chances > 0:
#                 new_pass = input("Re-enter password: ").upper()
#                 if users[username] == new_pass:
#                     print(f"\n✅ Welcome {username} sir ")
#                     break
#                 else:
#                     chances -= 1
#                     print(f"❌ Wrong password. Chances left: {chances}")

#             if chances == 0:
#                 print("\n⛔ Try after some time.")
#                 break

#     else:
#         print("\n⚠ Username not found.")
#         choice = input("Do you want to create account? (1 = Yes / 0 = No): ")

#         if choice == "1":
#             new_username = input("Enter new username: ").upper()
#             new_password = input("Enter new password: ").upper()

#             users[new_username] = new_password
#             save_users(users)

#             print("\n✅ Account created successfully.")

#             test_user = input("\nEnter username again: ").upper()
#             test_pass = input("Enter password again: ").upper()

#             if users[test_user] == test_pass:
#                 print(f"\n✅ Welcome {test_user} sir ")
#         else:
#             print("\n Thank you!")
#             break

    
#     again = input("\nEnter 1 to continue OR 0 to exit: ")
#     while again != "0" and again != "1":
#         again = input("Please enter only 1 or 0: ")

#     if again == "0":
#         print("\n✅ Program Ended.")
#         break







import json
import datetime
import os
import requests
import instaloader

FILENAME = "users.json"
API_KEY = "11a0e44ac16b777b5001974c9f8839c4"

def load_users():
    if not os.path.exists(FILENAME):
        users = {
            "DHANANJAY": {"password": "1234", "last_login": "Never"},
            "SHUBHAM": {"password": "1111", "last_login": "Never"},
            "GANESH": {"password": "2222", "last_login": "Never"},
            "ROHIT": {"password": "3333", "last_login": "Never"},
            "ROHAN": {"password": "4444", "last_login": "Never"}
        }
        with open(FILENAME, "w") as file:
            json.dump(users, file, indent=4)

    with open(FILENAME, "r") as file:
        return json.load(file)

def save_users(users):
    with open(FILENAME, "w") as file:
        json.dump(users, file, indent=4)

#Create Account 
def create_account(users):
    print("\nCreate New Account")

    while True:
        username = input("Enter new username: ").upper()
        if username in users:
            print("Username already exists. Try again.")
        else:
            break

    while True:
        password = input("Enter new password (min 6 characters): ").upper()
        if len(password) < 6:
            print("Password too short.")
        else:
            break

    users[username] = {
        "password": password,
        "last_login": "Never"
    }

    save_users(users)
    print("Account created successfully ✅")

# FIXED Weather Function
def show_weather():
    location = input("\nEnter your city name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if not isinstance(data, dict):
            print("Weather server error.")
            return

        if "main" not in data:
            print("City not found or API issue.")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        print(f"\nWeather in {location}")
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", desc)

    except Exception as e:
        print("Weather error:", e)

def check_instagram():
    choice = input("\nDo you want to see Instagram followers/following of anyone? (1/0): ")

    if choice == "0":
        print("Skipping Instagram feature.")
        return

    username = input("Enter Instagram username I'D: ").upper()

    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        print("\nInstagram Data")
        print("Username:", username)
        print("Followers:", profile.followers)
        print("Following:", profile.followees)

    except:
        print("No Instagram account found.")

def user_dashboard(username):
    print("\nWelcome,", username,"sir")
    print("Login successful and recorded.")

    show_weather()
    check_instagram()

    while True:
        choice = input("\nEnter 1 to continue or 0 to logout: ")

        if choice == "0":
            print("Thank you",username ,"for using the system ✅")
            exit()

        elif choice == "1":
            show_weather()
            check_instagram()

        else:
            print("Invalid input. Enter only 1 or 0.")

def login(users):
    username = input("\nEnter username: ").upper()

    if username not in users:
        print("User not found.")
        choice = input("Do you want to create account? (1/0): ")

        if choice == "1":
            create_account(users)
        else:
            print("Exiting...")
            exit()
        return

    attempts = 2

    while attempts > 0:
        password = input("Enter password: ").upper()

        if password == users[username]["password"]:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("\nWelcome",username,"Sir")
            print("Last Login:", users[username]["last_login"])
            print("Current Login:", current_time)

            users[username]["last_login"] = current_time
            save_users(users)

            user_dashboard(username)
            return

        else:
            attempts -= 1
            print("Wrong password. Attempts left:", attempts)

    print("Try again later.")

def main():
    print("\n->Python Login System with Weather & Instagram<-")
    users = load_users()

    while True:
        login(users)

main()