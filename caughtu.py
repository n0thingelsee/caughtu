import os
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import webbrowser
import time

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def finish():
	input("\n[ Press enter to continue ]")

green = "\x1b[32m"
white = "\x1b[37m"
red = "\x1b[31m"
purple = "\x1b[35m"
gray = "\x1b[90m"

logo = f"""{green}
 ██████╗ █████╗ ██╗   ██╗ ██████╗ ██╗  ██╗████████╗██╗   ██╗
██╔════╝██╔══██╗██║   ██║██╔════╝ ██║  ██║╚══██╔══╝██║   ██║
██║     ███████║██║   ██║██║  ███╗███████║   ██║   ██║   ██║
██║     ██╔══██║██║   ██║██║   ██║██╔══██║   ██║   ██║   ██║
╚██████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██║   ██║   ╚██████╔╝
 ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
                                                            
{gray}by n0thing.elsee                
"""

choices = f"""{white}
{purple}[01] {white}Track IP
{purple}[02] {white}Track Num
{purple}[03] {white}DoS Attack
{purple}[04] {white}Google Dorks
{purple}[05] {white}D0x Search
{purple}[06] {white}Osint AI

{purple}[00] {red}Exit
"""
while __name__ == "__main__":
	clear()
	print(logo)
	print(choices)
	i = int(input(f"{white}$ {green}/ {white}root/caughtu >> "))
	if i == 0:
		time.sleep(1)
		exit()
	elif i == 1:
		clear()
		ip = str(input("Insert the IP: "))
		r = requests.get(f"https://ipinfo.io/{ip}")
		print(r.json()), finish()
	elif i == 2:
		clear()
		raw_number = str(input("Digit the num (dont add any space): "))
		parsed_num = phonenumbers.parse(raw_number)
		clear()
		is_valid = phonenumbers.is_valid_number(parsed_num)
		location = geocoder.description_for_number(parsed_num, "en")
		service_provider = carrier.name_for_number(parsed_num, "en")
		time_zones = timezone.time_zones_for_number(parsed_num)
		print(f"Valid: {is_valid}")
		print(f"Location: {location}")
		print(f"Carrier: {service_provider}")
		print(f"Timezones: {time_zones}")
		finish()
	elif i == 3:
		clear()
		target = str(input("Type the target Domain (add https:// or http://)\n╚════► "))
		clear()
		while True:
			r = requests.get(target)
			if r.status_code == 200:
				print("Packet sented")
			else:
				print("Failed sent packets")
	elif i == 4:
		clear()
		print("[01] Track a Company")
		print("[02] Track a Person")
		i1 = int(input("\nSelect one: "))
		if i1 == 1:
			clear()
			company = str(input("Insert the Company name: "))
			company = company.replace(" ", "+")
			webbrowser.open(f'https://www.google.com/search?q="{company}"+filetype%3Apdf+OR+filetype%3Ajpg+OR+filetype%3Atxt+OR+filetype%3Apng')
			finish()
		elif i1 == 2:
			clear()
			print("[01] Track his Entire Life")
			print("[02] Track his Social Life")
			print("[03] Track his Accounts")
			i2 = int(input("\nSelect one: "))
			if i2 == 1:
				clear()
				name = input("Insert his first name: ")
				name = name.replace(" ", "+")
				surname = input("Insert his surname: ")
				surname = surname.replace(" ", "+")
				webbrowser.open(f"https://www.google.com/search?q=%22{name}%22+%22{surname}%22")
				finish()
			elif i2 == 2:
				clear()
				name = input("Insert his first name:")
				surname = input("Insert his surname: ")
				surname = surname.replace(" ", "+")
				name = name.replace(" ", "+")
				webbrowser.open(f"https://www.google.com/search?q=%22{name}%22+%22{surname}%22+site%3AYouTube.com+OR+site%3Afacebook.com+OR+site%3Ainstagram.com+OR+site%3ATikTok.com")
				finish()
			elif i2 == 3:
				clear()
				username = input("Insert a his common username: ")
				webbrowser.open(f"https://www.google.com/search?q=%22{username}%22+OR+%22%40{username}%22")
				finish()
	elif i == 5:
		clear()
		username = input("Insert a Username/Full Name: ")
		username = username.replace(" ", "+")
		webbrowser.open(f"https://doxbin.com/?search=content&query={username}")
		finish()
	elif i == 6:
		clear()
		search = str(input('tip: dont click "accept only necessary cookies" or "accept all cookies"\nInsert his username/Full name: '))
		newsearch = search.replace(" ", "%2520")
		newsearch0 = newsearch.replace("'", "%27")
		webbrowser.open("https://www.perplexity.ai/search/new?q=find%2520all%2520"+newsearch0+"%27s%2520information%2520on%2520the%2520web")
		finish()
