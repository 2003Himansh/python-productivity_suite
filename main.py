from calculator import calculator_menu
from notes_manager import notes_menu
from timer import timer_menu
from file_organizer import organize_files
from unit_converter import converter_menu
from utils import backup_data, restore_data


def main_menu():

    while True:

        print("\n================================")
        print(" PERSONAL PRODUCTIVITY SUITE ")
        print("================================")

        print("1. Calculator Tool")
        print("2. Notes Manager")
        print("3. Timer & Stopwatch")
        print("4. File Organizer")
        print("5. Unit Converter")
        print("6. Backup & Restore")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            calculator_menu()

        elif choice == "2":
            notes_menu()

        elif choice == "3":
            timer_menu()

        elif choice == "4":
            organize_files()

        elif choice == "5":
            converter_menu()

        elif choice == "6":

            print("1. Backup Data")
            print("2. Restore Data")

            c = input("Enter choice: ")

            if c == "1":
                backup_data()
            elif c == "2":
                restore_data()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()