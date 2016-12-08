import os

IMAGES_PATH = "/Users/ahararwala/Downloads/prank"


def rename_files():
    file_list = os.listdir(IMAGES_PATH)
    saved_dir = os.getcwd()

    os.chdir(IMAGES_PATH)

    for file_name in file_list:
        print ("Old Name= " + file_name)
        if file_name.startswith("."):
            continue
        newFileName = file_name.translate(None, "0123456789")
        print ("New Name=" + newFileName)

        os.rename(file_name, newFileName)

    os.chdir(saved_dir)


rename_files()
