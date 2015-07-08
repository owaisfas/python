import os
def rename_files():
    # get files names from a folder
    file_list = os.listdir(r"C:\OOP\prank")
    print(file_list)
    original_path = os.getcwd()
    os.chdir(r"C:\OOP\prank")
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(original_path)

rename_files()
