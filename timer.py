import time


def timer_menu():

    while True:

        print("\nTimer")
        print("1. Countdown Timer")
        print("2. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            seconds = int(input("Enter seconds: "))

            while seconds:

                mins, sec = divmod(seconds, 60)

                timer = f"{mins:02d}:{sec:02d}"

                print(timer, end="\r")

                time.sleep(1)

                seconds -= 1

            print("Time up!")

        elif choice == "2":
            break