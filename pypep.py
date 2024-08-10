import time
import os
#----------------------------------------------------------------------------------------------------------------------------------------
print("Launching PyPep...")
user_name = open('user.txt')
u_n = user_name.read()
user_pass = open('pass.txt')
u_p = user_pass.read()
time.sleep(4)
print("Welcome to PyPep,",u_n)
print("The OS Made with Python. Type help for more info")
passw = input("Enter your password:")
if passw == u_p:
  while True:
        print("Welcome to PyPep OS,",u_n)
        print("""
              [!] About OS
              [B] Extras
              [H] Terminal
              [C] Time Watch
              [+] Calculator
              [W] Weather
              [0-0] Reboot
              [-_-]Shut Down
                              """)
        
        app = input("[?]")
        if app == "!":
          print("Opening Info about OS. Please wait")
          time.sleep(1)
          os.startfile("AboutOS.py")
      
        if app == "H":
          print("Opening Terminal. Please wait")
          time.sleep(1)
          os.startfile("command.py")

        if app == "h":
          print("Opening Terminal. Please wait")
          time.sleep(1)
          os.startfile("command.py")


        if app == "B":
          print("Opening Extra Content. Please wait")
          time.sleep(1)
          os.startfile("extras.py")

        if app == "b":
          print("Opening Extra Content. Please wait")
          time.sleep(1)
          os.startfile("extras.py")

        if app == "C":
          print("Opening Time Watch. Please wait")
          time.sleep(2)
          os.startfile("clock.py")

        if app == "c":
          print("Opening Time Watch. Please wait")
          time.sleep(2)
          os.startfile("clock.py")

        if app == "W":
          print("Loading Weather app... It would take 5 secs...")
          time.sleep(5)
          os.startfile("weather.py")

        if app == "w":
          print("Loading Weather app... It would take 5 secs...")
          time.sleep(5)
          os.startfile("weather.py")


        
        if app == "0-0":
          print("Rebooting. Please wait")
          time.sleep(5)
          os.startfile("pypep.py")
          exit()

        if app == "-_-":
          print("Shutting down. Please wait")
          time.sleep(5)
          exit()
  
        if app == "+":
          print("Loading Calculator. This may take a while...")
          time.sleep(4)
          os.startfile("calc.py")


          print("Welcome aboard")
else:                        
    print("wrong!")