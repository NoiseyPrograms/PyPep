#PyPep OS
import time
import  os

os.system("cls")
print("Loading.")
time.sleep(2)
print("Loading..")
time.sleep(2)
print("Loading...")
time.sleep(1)
print("Macrohard PyPep OS v1.2.2.3 Made with python")
ask = input("Have an account yet?")
if ask == "Yes":
    time.sleep(2)
    os.startfile("pypep.py")
elif ask == "yes":
    time.sleep(2)
    os.startfile("pypep.py")

elif ask == "Y":
    time.sleep(2)
    os.startfile("pypep.py")

elif ask == "y":
    time.sleep(2)
    os.startfile("pypep.py")
else:
    user = input("Enter your username [?]")
    password = input("Enter your password [?]")
    f = open('user.txt','w')
    f.write(user)
    f.close()
    f = open('pass.txt','w')
    f.write(password)
    print("Now loading Main OS Files,please wait...")
    time.sleep(4)
    os.startfile("pypep.py")
    f.close()