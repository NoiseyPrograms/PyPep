import time
import os
import pyautogui
import psutil
#---------------
os.system("cls")

print("PyTerm Version 1.0.0")

term = input("TermPy: ")
while True:
    if term == "Boost PC":
        pyautogui.hotkey('win' , 'r')
        time.sleep(2)
        pyautogui.typewrite('powershell')
        time.sleep(2)
        pyautogui.press('enter')
        pyautogui.typewrite('%temp%')

        pyautogui.press('enter')
        time.sleep(2)
        exit()

    if term == "open msedge.exe":
        pyautogui.hotkey('win' , 'r')
        time.sleep(1)
        pyautogui.typewrite('msedge.exe')
        time.sleep(1)
        pyautogui.press('enter')
        exit()

    if term == "open regedit.exe":
        pyautogui.hotkey('win' , 'r')
        time.sleep(1)
        pyautogui.typewrite('regedit.exe')
        time.sleep(1)
        pyautogui.press('enter')
        exit()

    if term == "help":
     time.sleep(2)
     print("""
Help   Help Menu
open msedge.exe   Opens Microsoft Edge for you
open regedit.exe   Opens Regestry Edit (Optional Command)
Boost pc   Opens '%Temp%' folder for you. If you delete necessary folders (half or all),you will boost your pc like this
More commands comming soon""")
     term = input("TermPy: ")