#Author Constantinos Charalambous

'''This is completed code which will take the ip's in the list, look through
all of the hitcnt files in the folder and extract 0 hit count for specific ip's
'''

import glob, os
import time

mylist = []

def find_zeros():

    hits = 'hitcnt=0'
    ips = ['10.5.x.x',	'10.5.x.x',	'172.x.x.x']

    for filename in os.listdir('c:\\hitcnt'):
        with open(os.path.join('C:\\hitcnt', filename)) as f:
            print(f)
            x = f.readlines()

            for i in x:
                for j in ips:
                    if hits in i and j in i:
                        with open('zeros.txt', 'a') as newfile:
                            y = newfile.writelines(filename + ' ' + i)

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
        del i[-2:]
    
    for i in mylist:
        i.insert(0, 'no')

def convert():

    user_name = input("Enter employee number: ")
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
#rem_files()