Project Statement: Weather & Social Tracker
1. Problem Statement
I noticed that I often have to switch between different apps just to check basic things like the weather or my Instagram follower count. It feels inefficient to open a browser or mobile app for every small task.

My goal with this project is to build a simple "all-in-one" terminal tool. It combines a secure login system with a dashboard that pulls live weather data and Instagram stats, so I can see everything in one place using the command line.

2. Project Scope
This project focuses on backend logic and API integration using Python.

What I will build:

A user authentication system (Login/Sign up) to secure the app.

Data persistence using a JSON file to store user credentials safely.

Integration with the OpenWeather API to fetch real-time temperature and conditions.

Integration with the Instaloader library to fetch follower/following counts.

A Command Line Interface (CLI) menu for easy navigation.

What is NOT included (Limitations):

No Graphical User Interface (GUI); it will run entirely in the terminal.

No complex databases (like SQL); I am using JSON for simplicity.

No mobile or web version.

3. Target Audience
This tool is designed for:

Students and beginners who want to see how APIs work in Python.

Developers who prefer using the terminal over opening web browsers.

Anyone looking for a lightweight utility to check daily stats.

4. Key Features
Secure Login: Users can create an account and log in with a password.

Weather Checker: Users can type a city name to get the current weather description and temperature.

Instagram Stats: Shows the user's current follower and following count.

JSON Storage: Automatically saves user data and login history to a local file.
