import time
import os
import pyautogui
import psutil
#---------------
os.system("cls")

print("PyTerm Version 1.0.0")

term = input("TermPy: ")
while True:
    if term == "Boost pc":
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
        