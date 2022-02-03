import webbrowser
import pyautogui as gui
import keyboard
import time
import string

# ---------------------new numbers------------------#
chatposition = (2850, 1028)

numbers = open("number.txt", "r")
message = open("message.txt", "r", encoding="utf8")
old_message = message.read()
message = """"""
for i in old_message:
    if i == "\n":
        message = message + " "
    else:
        message = message + i
numbers = numbers.read()
numbers = numbers.split(",")
limit = int(input("limit the usage : "))
repeat = int(input("repeat : "))
new_number = []

# # ---------------handel the new numbers--------------#
for number in numbers:
    for x in string.ascii_letters:
        number = number.replace(x + ",", "")
        number = number.replace(x, "")
    number = number.replace("+", "'+")
    number = number.replace(",", "',")
    number = number.replace(", ", ",")
    number = number.replace(" ", "")
    number = number.replace("+2", "")
    number = number.replace("'1", "'01")
    number = number.replace("-", "")
    number = number.replace("+", "")
    for x in range(11):
        number = number.replace("'1", "'")
        number = number.replace("'2", "'")
        number = number.replace("'3", "'")
        number = number.replace("'4", "'")
        number = number.replace("'5", "'")
        number = number.replace("'6", "'")
        number = number.replace("'7", "'")
        number = number.replace("'8", "'")
        number = number.replace("'9", "'")
        number = number.replace("'00", "'")
        number = number.replace("'02", "'")
        number = number.replace("'03", "'")
        number = number.replace("'04", "'")
        number = number.replace("'05", "'")
        number = number.replace("'06", "'")
        number = number.replace("'07", "'")
        number = number.replace("'08", "'")
        number = number.replace("'09", "'")
        number = number.replace("'',", "")
    number = number.replace("'", "")
    number = number.replace(
        ",",
        """
    """,
    )
    new_number.append(number)

# # -------------------run------------------------#
sent_msgs = 0
while True:
    if sent_msgs >= limit and limit != "unlimted":
        print("done successfully")
        exit()
    url = (
        "https://web.whatsapp.com/send?phone=%2B2"
        + new_number[sent_msgs]
        + "&text&app_absent=0"
    )
    # ----------------------------------------
    webbrowser.open(url)
    time.sleep(20)
    for i in range(repeat):
        gui.click(chatposition)
        keyboard.write(message)
        gui.press("enter")
    time.sleep(5)
    sent_msgs += 1
    keyboard.press_and_release("ctrl+w")
# ------------------------- mkan el mouse ---------------#

# while True:
#     print(gui.position())
