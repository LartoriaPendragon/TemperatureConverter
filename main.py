# Ask user whether they want to convert from C -> F or F -> C
# Take in the value and compute the result using this formula (0°C × 9/5) + 32 = 32°F or (32°F − 32) × 5/9 = 0°C
# Return this to user with the option to go again indefinitely

print("This is a calculate that converts between Celsius and Fahrenheit and vice versa")

while True:

    choice = input("If you're trying to calculate fahrenheit type F if Celsius type C")
    end = input("Would you like to exit this program")
    if end == "yes":
        break

    if choice == "F":
        choice_f = int(input("Whats the temperature in celsius?"))
        choice_f_result = choice_f * 9 / 5 + 32
        print("The temperature in Fahrenheit is", choice_f_result)

    else:
        choice == "C"
        choice_c = int(input("Whats the temperature in fahrenheit?"))
        choice_c_result = (choice_c - 32) * 5 / 9
        print("The temperature in celsius is", choice_c_result)



