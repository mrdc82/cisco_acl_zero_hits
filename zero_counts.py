import tkinter as tk
from tkinter import filedialog
import glob, os
import time

if 'zeros.txt' in os.listdir():
    print('Files validated')
    print('Select your file')
else:
    open('zeros.txt', 'a').close()
    print('File validation complete')
    print('Select your file')

def find_zeros():
    
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print('File loading, please wait')
    input('File loaded, press any key to run')
    
    with open(file_path, 'r') as file:
        x = file.readlines()

    hits = 'hitcnt=0'

    for i in x:
        if hits in i:
            with open('zeros.txt', 'a') as newfile:
                y = newfile.writelines(i)

mylist = []

def rem_rules():
    
    with open('zeros.txt','r') as file:
        x = file.readlines()

        global mylist

        for i in x:
            i = i.strip()
            i = i.split(' ')
            mylist.append(i)

def rem_text():
    for i in mylist:
        del i[2:4]
        del i[-6:]
    
    for i in mylist:
        i.insert(0, 'no')

def convert():

    user_name = input("Filename: ")
    timestr = time.strftime("%Y%m%d%H%M%S")

    file_name = '{0}-{1}'.format(user_name, timestr)
    print(file_name)

    for j in mylist:
        j = ' '.join(j)
        with open(file_name, 'a+') as outfile:
            outfile.writelines(j + '\n')

def rem_files():
    os.remove('zeros.txt')

find_zeros()
rem_rules()
rem_text()
convert()
rem_files()