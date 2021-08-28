from pyfiglet import Figlet
from termcolor import colored
import os
import time,sys
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

f = Figlet(font='5lineoblique')

print(colored(f.renderText('PhoneInfo'),color = 'magenta'))
print("\n\n")



msg0=(colored('''+----------------------------------------------+
| Name:        PhoneNumber Validator V1
| Author:      @LuciferxD,@LegendPikachu_YT
+----------------------------------------------+\n''',color = 'blue'))
for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02) 
c = colored("\n\nARE YOU SURE YOU WANT TO START (y/n) = ", color = 'red')
d = input(c).lower()
if d == "y":
	b = (colored("Time Zone = ",color = 'cyan'))
	ae1 = input("\n\nEnter Your Phone Number (With Country code and Include + ) = ")

	phone_number = phonenumbers.parse(ae1)
	os. system('clear')
	print(colored("Phone Number = " + ae1,color = 'cyan'))
	print(("Country = ") + geocoder.	description_for_number (phone_number, "en"))
	print(("Carrier = ") + carrier.name_for_number (phone_number, "en"))
	timeZone = timezone.time_zones_for_number(phone_number)
	print(b , timeZone)
	print(colored("\n\n\n\t#Note - This is V1 Of This Tool ,\n This only Supports Indian Number\n In Next Update We Will Add Many Features\n Like State,Name and Will Support More Country \nUntill Than Bye Bye!",color = 'red'))
elif d == "n":
	print(colored("\n\nExiting The Tool",color = 'yellow'))
	exit
else:
	print(colored("\n\nSorry, Senpai But This Is Not A Valid Function",color = 'green'))
	exit