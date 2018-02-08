import os

def rename_files():
    # get files names
    file_list = os.listdir(r"C:\Users\michael.gavidia\Downloads\Slack Downloads")
    print(file_list)

    # for each files, rename it
    for file_name in file_list:
        os.rename(file_name,)
rename_files()
