import os
import shutil


def organize_files():

    folder = input("Enter folder path: ")

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        if os.path.isfile(path):

            ext = file.split(".")[-1]

            new_folder = os.path.join(folder, ext)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            shutil.move(path, os.path.join(new_folder, file))

    print("Files organized successfully")