# -------------------- Morse Code ------------------------------ #
# 1. The first thing to do was to investigate what Morse Code is, because
# I had no idea how the code works, the next pages help me to understand the structure
# https://en.wikipedia.org/wiki/Morse_code
# https://morsecode.world/international/translator.html
# https://future-seafarer.com/morse-code/#:~:text=SPACE%20BETWEEN%20DOT%20OR%20DASH,Space%20Equal%20To%20Seven%20Dots.

# 2. Now the next step is to decide how to translate a user's input to a
# morse code. I came up with the idea of using an API to avoid writing down
# all the symbols for each letter, number into the morse code.

# So I am going to use the next API to get the morse code
# https://funtranslations.com/api/morse

import requests
from title import header

continue_translating = True
print(header)


while continue_translating:
    print("This program translater Morse Code using an API, Type the option you want to execute: ")
    print("1. From English to Morse Code")
    print("2. From Morse Code to English")
    choice = input("Your choice: ")
    valid_choice = choice == "1" or choice == "2"
    while not valid_choice:
        print("Sorry, that is not a valid option, Select one of the next: ")
        print("1. From English to Morse Code")
        print("2. From Morse Code to English")
        choice = input("Your choice: ")
        valid_choice = choice == "1" or choice == "2"

    if choice == "1":
        user_text = input("Please enter the English Text to translate into Morse Code: ")
        parameters = {
            "text": user_text
        }

        response = requests.get(url="https://api.funtranslations.com/translate/morse.json", params=parameters)
        response.raise_for_status()  # This code returns the error code in case there would be one
        morse_data = response.json()  # Once our request succeeded we can get the data
        translation = morse_data["contents"]["translated"]
        print("The translation for the text from English to Morse Code you enter is the next: ")
        print(translation)
    else:
        morse_code = input("Please enter the Morse Code to translate into English: ")
        parameters = {
            "text": morse_code
        }
        response = requests.get(url="http://api.funtranslations.com/translate/morse2english.json", params=parameters)
        response.raise_for_status()  # This code returns the error code in case there would be one
        english_text_data = response.json()  # Once our request succeeded we can get the data
        english_translation = english_text_data["contents"]["translated"]
        print("The translation for the text from Morse Code to English you enter is the next: ")
        print(english_translation)

    want_continue = input("Do you want to translate again Y/N: ").lower()
    valid_answer = want_continue == "y" or want_continue == "n"
    while not valid_answer:
        print("Sorry that is not a valid option")
        want_continue = input("Do you want to translate again Y/N: ").lower()
        valid_answer = want_continue == "y" or want_continue == "n"
    if want_continue == "n":
        continue_translating = False

print("Thank you for using the program 🤗")

