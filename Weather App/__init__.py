import requests
import json
import pyttsx3

print("Welcome to Weather App ::::::\n")
print("Created by Harsh Mishra ::::::\n")
engine = pyttsx3.init()
engine.say("Welcome to Weather App")
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Created by Harsh Mishra ")
engine.runAndWait()

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=55939d48a00b4ce9ba3220347230406&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

while True:
    print("\n--- Menu ---")
    print("1. Show current temperature")
    print("2. Show current weather condition")
    print("3. Show humidity")
    print("4. Show wind speed")
    print("5. Show pressure")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        print(f"The current temperature in {city} is {w} degrees Celsius")
        engine = pyttsx3.init()
        engine.say(f"The current temperature in {city} is {w} degrees Celsius")
        engine.runAndWait()
    elif choice == "2":
        condition = wdic["current"]["condition"]["text"]
        print(f"The current weather condition in {city} is {condition}")
        engine = pyttsx3.init()
        engine.say(f"The current weather condition in {city} is {condition}")
        engine.runAndWait()
    elif choice == "3":
        humidity = wdic["current"]["humidity"]
        print(f"The current humidity in {city} is {humidity}%")
        engine = pyttsx3.init()
        engine.say(f"The current humidity in {city} is {humidity}%")
        engine.runAndWait()
    elif choice == "4":
        wind_speed = wdic["current"]["wind_kph"]
        print(f"The current wind speed in {city} is {wind_speed} kilometers per hour")
        engine = pyttsx3.init()
        engine.say(f"The current wind speed in {city} is {wind_speed} kilometers per hour")
        engine.runAndWait()
    elif choice == "5":
        pressure = wdic["current"]["pressure_mb"]
        print(f"The current pressure in {city} is {pressure} millibars")
        engine = pyttsx3.init()
        engine.say(f"The current pressure in {city} is {pressure} millibars")
        engine.runAndWait()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Thank you for using the Weather App!")
