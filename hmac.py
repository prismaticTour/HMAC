import pickle
import os
import hmac
from hashlib import md5
import getpass
import sys

key = b'cryptography'
dataset = []
users = []
outputFile_1 = 'login.data'
outputFile_2 = 'users.data'


def login_check() :
	global dataset
	global users

	os.system('clear')

	if os.path.exists(outputFile_2):
		with open(outputFile_2,'rb') as rfq: 
			users = pickle.load(rfq)

	if os.path.exists(outputFile_1):
		with open(outputFile_1,'rb') as rfp: 
			dataset = pickle.load(rfp)

	print ("\t\t|||--- LOGIN ---|||")

	u_name = raw_input('\n\tUsername : ')
	pword = bytes(getpass.getpass('\tPassword : '))

	h = hmac.new(key,pword,md5)
	login = u_name, h.hexdigest()

	if os.path.exists(outputFile_1) and os.path.exists(outputFile_2) :
		if u_name not in users :
			new_user(login,u_name)

		elif u_name in users and login not in dataset :
			print ("Incorrect Password.")
			sys.stdin.read(1)
			login_check()

		else :
			print ("\n\nLogin Successful")
			sys.stdin.read(1)

	else :
		new_user(login, u_name)
        
        
def new_user(login,u_name) :
	global dataset
	global users

	flag = raw_input("\n\nNew User ID detected.\nAdd user ? (Y / N ) : ")

	if(flag.lower()=='y') :
		a_pword = bytes(getpass.getpass('\nEnter Admin Password : '))
		h = hmac.new(key,a_pword,md5)
    	
		if h.hexdigest()=='bf8fc2281e5bd5ee23320d1b4bb44a5c' :
			dataset.append(login)
			users.append(u_name)

			with open(outputFile_1,'wb') as wfp:
				pickle.dump(dataset, wfp)
			with open(outputFile_2,'wb') as wfq:
				pickle.dump(users, wfq)

			with open(outputFile_1,'rb') as rfp:
				dataset = pickle.load(rfp)
			with open(outputFile_2,'rb') as rfq:
				users = pickle.load(rfq)

			print ("User Added.")
			sys.stdin.read(1)
			print("\nProceed to login")
			sys.stdin.read(1)
			os.system('clear')
			login_check()

		else :
			print ("Incorrect Password.")
			sys.stdin.read(1)
			os.system('clear')
			new_user(login)

	elif(flag.lower()=='n') :
		os.system('clear')
		login_check()

	else :
		print ("Incorrect Entry")
		sys.stdin.read(1)
		os.system('clear')
		new_user(login, u_name)

login_check()