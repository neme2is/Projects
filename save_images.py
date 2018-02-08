# coding: UTF-8
import requests
import os
import time

saveLocation = input('Please specifiy a folder name to save to: ')
env = input('Environment to downlaod from (ie. www or a.qtest): ')
doc = input("Enter or drag text file for importing: ")
urlConfirm = 'https://' + (env) + '.abcmouse.com'
url = 'https://' + (env) + '.abcmouse.com/artwork/html5/abc/path_section/'
images = []
total_files = len(images)
fullPath = os.path.realpath(saveLocation)
n = 0
i = 0
u = False

#with open((doc), 'r') as myfile:
#with open(doc) as myfile:
#    data=myfile.read()
#    images = data.split(", ")

#def confirmInput():
#    print()
#    print('Save folder is ' + '"' + (saveLocation) + '".')
#    print('Download form ' + (urlConfirm))
#    print('Number of files to downlaod is ' + str(total_files) + '.')
#
#def confirmResponse():
#    input('Is this correct? yes/no: ')

def userIn():
    print('Please specifiy a folder name to save to: ')
    saveLocation = input()
    print('Environment to downlaod from (ie. www or a.qtest): ')
    env = input()
    print("Enter or drag text file for importing in csv format: ") # filenames should be in csv format
    doc = input()
    with open(doc) as myfile:
        data=myfile.read()
        images = data.split(", ")

# creates a folderse for saving the files
def createFolder():
    if os.path.exists(saveLocation) == True: # checks to see if the folder already exists, if so skips
        print('Directory already exists.')
        time.sleep(1)
        print('Starting to download files...')
        time.sleep(2)
    elif os.path.exists(saveLocation) == False: # if folder does not exist, it creates the folder
        os.makedirs(saveLocation)
        print('Directory has been created.')
        time.sleep(1)
        print('Starting to download files...')
        time.sleep(2)

def downloadImages():
    urlImage = (url + images[n])
    res = requests.get (urlImage)
    playFile = open((saveLocation) + '/' + (images[n]) + '.png ', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
        playFile.close()
    print('Downloaded '+ images[n])

def completeTask():
    print('Downloading of requested files is complete!')
    time.sleep(2)
    input('Press any key to exit.')

# start downloading the images/files
with open(doc) as myfile: # converts the text file into a reabable list
    data=myfile.read()
    images = data.split(", ")

createFolder()

for items in images: # goes through the list and downloads each file
    downloadImages()
    n += 1

# provides output on what was done and ends the script
if n == len(images):
    fileList = os.listdir(saveLocation) # looks at the files in the saved location
    number_files = len(fileList) # counts the number of files in saved location
    #print(str(n) + ' files processed. ' + str(number_files) + ' files saved to ' + '"' + (fullPath) + '"'+ '.')
    print(str(n) + ' files processed.')
    print(str(number_files) + ' files saved to ' + '"' + (fullPath) + '"'+ '.')
    print()
    completeTask()
