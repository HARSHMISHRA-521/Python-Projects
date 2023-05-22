# Exercise 11 - Drink Water Reminder (Solution)
# Write a python program which reminds you of drinking water every
# hour or two. Your program can either beep or send desktop notifications
# for a specific operating system


import time
from plyer import notification

def show_notification(title, message):
    notification.notify(title=title, message=message, timeout=10)

def drink_water_reminder(interval):
    while True:
        show_notification("Drink Water Harsh", "Remember to drink water!")
        time.sleep(interval)

# Set the reminder interval (in minutes)
reminder_interval = 10

drink_water_reminder(reminder_interval)


# import time
# from win10toast import ToastNotifier
# import win32api
#
# def show_notification(title, message):
#     toaster = ToastNotifier()
#     toaster.show_toast(title, message, duration=10)
#
# def drink_water_reminder(interval):
#     while True:
#         show_notification("Drink Water Harsh", "Remember to drink water!")
#         time.sleep(interval)
#
# # Set the reminder interval (in minutes)
# reminder_interval = 60
#
# drink_water_reminder(reminder_interval)
#
# # Define a function to handle Windows messages
# def WNDPROC(hwnd, msg, wParam, lParam):
#   # Return the default window procedure
#   return win32api.DefWindowProc(hwnd, msg, wParam, lParam)
