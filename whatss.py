import webbrowser
import pyautogui as gui
import keyboard
import time 
import string
import random
#---------------------new numbers------------------#
new_numbers = input("new numbers : ")
file_name = input("name the output file : ")

#---------------handel the new numbers--------------#
for x in string.ascii_letters:
    new_numbers = new_numbers.replace(x+",", "")
    new_numbers = new_numbers.replace(x, "")
new_numbers = new_numbers.replace("+", "'+")
new_numbers = new_numbers.replace(",", "',")
new_numbers = new_numbers.replace(", ", ",")
new_numbers = new_numbers.replace(" ", "")
new_numbers = new_numbers.replace("+2", "")
new_numbers = new_numbers.replace("'1", "'01")
new_numbers = new_numbers.replace("-", "")
new_numbers = new_numbers.replace("+", "")
for x in range(11):
    new_numbers = new_numbers.replace("'1", "'")
    new_numbers = new_numbers.replace("'2", "'")
    new_numbers = new_numbers.replace("'3", "'")
    new_numbers = new_numbers.replace("'4", "'")
    new_numbers = new_numbers.replace("'5", "'")
    new_numbers = new_numbers.replace("'6", "'")
    new_numbers = new_numbers.replace("'7", "'")
    new_numbers = new_numbers.replace("'8", "'")
    new_numbers = new_numbers.replace("'9", "'")
    new_numbers = new_numbers.replace("'00", "'")
    new_numbers = new_numbers.replace("'02", "'")
    new_numbers = new_numbers.replace("'03", "'")
    new_numbers = new_numbers.replace("'04", "'")
    new_numbers = new_numbers.replace("'05", "'")
    new_numbers = new_numbers.replace("'06", "'")
    new_numbers = new_numbers.replace("'07", "'")
    new_numbers = new_numbers.replace("'08", "'")
    new_numbers = new_numbers.replace("'09", "'")    
    new_numbers = new_numbers.replace("'',", "")    
new_numbers = new_numbers.replace("'", "")
new_numbers = new_numbers.replace(",", '''
''')
#----------------------write-------------------#
with open(file_name + '.txt', 'a') as file:
    print()
with open(file_name + '.txt', 'r+') as file:
    for line in file:
        if new_numbers in line:
           break
    else:    
        file.write(new_numbers + "\n")
#target_place = input ("target place : ")
target_place = file_name
limite = input ("limite the usage : ")
check = limite.isdigit()
if ((check == False) and (limite != "unlimted")):
    exit()
message = input ("message : ")
#-------------------read------------------------#
with open(target_place + '.txt') as f:
    number = [line.rstrip() for line in f]
#-------------------run------------------------#    
sent_msgs=0
while True:
    if (str(sent_msgs) >= limite  and limite != "unlimted"):
        print ("done successfully")
        exit()    
    #number[sent_msgs] = '01119727679' #spam for one number
    url = 'https://web.whatsapp.com/send?phone=%2B2'+ number[sent_msgs] +'&text&app_absent=0'
    print (number[sent_msgs])
#----------------------------------------
    webbrowser.open(url)
    time.sleep(5)
    #gui.click(chatposition)#for now mish bnst8dmo
    keyboard.write(message)
    gui.press('enter')
    time.sleep(1)
    sent_msgs = sent_msgs + 1    
    print (sent_msgs)
    time.sleep(1)
    keyboard.press_and_release('ctrl+w')
    gui.press('enter')
#------------------------- mkan el mouse ---------------#
#print (gui.position())