import shutil
import datetime


def backup_data():

    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_file = f"data/backups/notes_backup_{now}.json"

    shutil.copy("data/notes.json", backup_file)

    print("Backup created:", backup_file)


def restore_data():

    file = input("Enter backup filename: ")

    shutil.copy(f"data/backups/{file}", "data/notes.json")

    print("Data restored")