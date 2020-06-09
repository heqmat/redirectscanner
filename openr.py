
import requests
import sys
import time
import os
from datetime import datetime

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
'''print("#################################################")
print("# Open redirect Scanner for dummies like me :)  #")
print("#  by ak1t4 (know.0nix@gmail.com)               #")
print("#  twitter.com/knowledge_2014               #")
print("#  www.security-root.com                #")
print("#################################################")
print("")
print("Use ./redirect.py [subdomains.file] [redirect-payload]")
print("Example ./redirect.py uber.list '//yahoo.com/%2F..'") '''

print(bcolors.CYAN + """ 
 ▒█████   ██▓███  ▓█████  ███▄    █  ██▀███  ▓█████ ▓█████▄ 
▒██▒  ██▒▓██░  ██▒▓█   ▀  ██ ▀█   █ ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌
▒██░  ██▒▓██░ ██▓▒▒███   ▓██  ▀█ ██▒▓██ ░▄█ ▒▒███   ░██   █▌
▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ ▓██▒  ▐▌██▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌
░ ████▓▒░▒██▒ ░  ░░▒████▒▒██░   ▓██░░██▓ ▒██▒░▒████▒░▒████▓ 
░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ 
  ░ ▒ ▒░ ░▒ ░      ░ ░  ░░ ░░   ░ ▒░  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒ 
░ ░ ░ ▒  ░░          ░      ░   ░ ░   ░░   ░    ░    ░ ░  ░ 
	░ ░              ░  ░         ░    ░        ░  ░   ░    
													 ░      
	  Open Redirect Scanner - Edited again by Heqmat
				  Developer is Ak1T4
										  
 

 """ + bcolors.RESET)


# Payloads example

#payload = '//www.google.com/%2F..'
#payload2 = '//www.yahoo.com//'
#payload3 = '//www.yahoo.com//%2F%2E%2E'

# first argument - file with subdomains

file = sys.argv[1]

# second argument - payload string

payload = sys.argv[2]



#open file with subdomains and iterates
 
with open(file) as f:

		print("================================================================================")
		print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "]" + " [" + bcolors.OKBLUE + "INFO" + bcolors.ENDC + "] " + "Searching the ex-girlfriend target &  Holy Grial at [303 see others]..")
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
				print("[" + bcolors.PURPLE + datetime.now().strftime('%H:%M:%S') + bcolors.RESET + "] " + "User quit...")
