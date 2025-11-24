Python Login System (Weather + Instagram)
Project Overview
This is a command-line tool I built to practice backend logic in Python. It combines a secure login system with API integrations to fetch real-time data.

What it does:

User System: Allows users to Sign Up and Login. It saves credentials and login history locally using a JSON file (so data persists even after closing the program).

Weather: Fetches live temperature and conditions for any city using the OpenWeatherMap API.

Instagram Analytics: Uses the instaloader library to grab follower/following counts for public profiles.

Features
Persistent Storage: Uses users.json as a lightweight database to store user details.

Live Data: Connects to the internet to get real-time weather and social stats.

Error Handling: I added checks for invalid passwords (limit of 2 attempts), wrong city names, and internet connection issues.

Simple Interface: Runs entirely in the terminal with a menu-based navigation.

Libraries Used
requests (for calling the Weather API)

instaloader (for scraping Instagram data)

json (built-in, for saving user data)
Setup & Installation
1. Install Dependencies You will need to install the external libraries first. Open your terminal and run:

Bash

pip install requests instaloader
2. Configure the Weather API You need a free API key from OpenWeatherMap for the weather feature to work.

Open main.py

Find the line: API_KEY = "Place_Your_Key_Here"

Replace it with your actual key.

How to Run
Clone or download this folder.

Navigate to the folder in your terminal:

Bash

cd your-project-folder
Run the script:

Bash

python main.py
Known Issues / Notes
Instagram Limitations: The instaloader library sometimes fails if you check too many profiles quickly because Instagram limits anonymous requests. If it fails, try again in a few minutes.

Security: Currently, passwords are saved as plain text in the JSON file. In a real-world app, I would hash these for security.

Future Plans
Add a basic GUI using Tkinter so it's not just text-based.

Implement password hashing to make it secure.

Add an option to delete your account from the JSON file.
