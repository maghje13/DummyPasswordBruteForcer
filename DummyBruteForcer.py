import random
import pyautogui
import string
import os

attempt = 1

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# chars = string.printable
chars_list = list(chars)


password = pyautogui.password("Enter a password : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print(str(guess_password) + " > " + str(attempt))
    attempt = int(attempt) + 1

    if(guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break

