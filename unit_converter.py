def converter_menu():

    while True:

        print("\nUnit Converter")
        print("1. KM to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            km = float(input("Enter KM: "))
            print("Miles:", km * 0.621371)

        elif choice == "2":

            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", (c * 9/5) + 32)

        elif choice == "3":
            break