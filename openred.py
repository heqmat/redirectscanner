# Open Redirect Scanner by heqmat

#Legal responsbility: 

#Usage of Forgery Tool for attacking targets without prior mutual consent is illegal. 
#It is the end user's responsibility to obey all applicable local, state and federal laws. 
#Developers assume no liability and are not responsible for any misuse or damage caused by this program.
#hemirguner@outlook.com



import requests
import sys
import time
import os
import urllib.request
import argparse
import datetime
import subprocess
import random


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	PURPLE = '\033[90m'
	CYAN = '\033[0;36;47m'
	RED   = "\033[1;31m"  
	CYAN  = '\033[1;36m'
	GREEN = "\033[0;32m"
	RESET = "\033[0;0m"
	BOLD    = "\033[;1m"
	REVERSE = "\033[;7m"

os.system('clear')
version = 1.2

print(bcolors.CYAN + f""" 

	 ▒█████   ██▓███  ▓█████  ███▄    █  ██▀███  ▓█████ ▓█████▄ 
	▒██▒  ██▒▓██░  ██▒▓█   ▀  ██ ▀█   █ ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌
	▒██░  ██▒▓██░ ██▓▒▒███   ▓██  ▀█ ██▒▓██ ░▄█ ▒▒███   ░██   █▌
	▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ ▓██▒  ▐▌██▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌
	░ ████▓▒░▒██▒ ░  ░░▒████▒▒██░   ▓██░░██▓ ▒██▒░▒████▒░▒████▓ 
	░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ 
	  ░ ▒ ▒░ ░▒ ░      ░ ░  ░░ ░░   ░ ▒░  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒ 
	░ ░ ░ ▒  ░░          ░      ░   ░ ░   ░░   ░    ░    ░ ░  ░ 
		░ ░              ░  ░         ░    ░        ░  ░   ░    

		                Version   {version}										     
	      Open Redirect Scanner - Edited again by Heqmat
====================================================================================

Usage of Forgery Tool for attacking targets without prior mutual consent is illegal. 
It is the end user's responsibility to obey all applicable local, state and federal laws. 
Developers assume no liability and are not responsible for any misuse or damage caused by this program.										  
 

 """ + bcolors.RESET)

# first argument - file with subdomains

file = sys.argv[1]

# second argument - payload string

payload = sys.argv[2]

def asd():
	
	from datetime import datetime
	with open(file) as f:
		

		print("================================================================================")
		print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "]" + " [" + bcolors.OKBLUE + "INFO" + bcolors.ENDC + "] " + "Searching..")
		print("================================================================================")
		time.sleep(4)


			# loop for find the trace of all requests (303 is an open redirect) see the final destination

		for line in f:

			try:


				line2 = line.strip()

				line3 = 'http://' + line2 + payload

				print(line3)

				response = requests.get(line3, verify=True)    

				print(response)

				try:
				

					if response.history:
						
								 
						print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "] " + "[" + bcolors.OKBLUE + "INFO" + bcolors.ENDC + "] " + "Request was redirected.")
									

						for resp in response.history:
							

			
							print("|")
							print(resp.status_code, resp.url)
										

							print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "] " + "[" + bcolors.OKBLUE + "INFO" + bcolors.ENDC + "] " + "Final destination:")


							print(bcolors.OKGREEN + "+" + bcolors.ENDC)
							print(response.status_code, response.url)

									
					else:

						print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "] " + "[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "] " + "Request was not redirected")

								
				except:
					
								
					print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "] " + "[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "] " + "Connection Error!!!")

			except:
				print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "] " + "Quiting...(A problem may have occurred.)")



#Check internet connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

if connect():                
    asd()
else:
    print("[" + bcolors.FAIL + "ERROR" + bcolors.ENDC + "] " + "You do not have an internet connection or not enough. Please check your internet connection and try again.") # dont have internet connection

# Payloads example

#payload = '//www.google.com/%2F..'
#payload2 = '//www.yahoo.com//'
#payload3 = '//www.yahoo.com//%2F%2E%2E'





#open file with subdomains and iterates
