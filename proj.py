import pickle
import os
import hmac
from hashlib import md5


def login_check() :
    key = b'cryptography'
    dataset = []
    outputFile = 'login.data'

    if os.path.exists(outputFile):
        with open(outputFile,'rb') as rfp: 
            dataset = pickle.load(rfp)

    u_name = raw_input('Username : ')
    pword = bytes(raw_input('Password : '))

    h = hmac.new(key,pword,md5)
    login = u_name, h.hexdigest()

    if login in dataset :
        print ("Login Successful")

    else :
        new_user(login,dataset,outputFile)
        
def new_user(login,dataset,outputFile) :
    flag = raw_input("New User ID detected.\n\nAdd user ? (Y / N ) : ")

    if(flag=='y') :
        dataset.append(login)
        with open(outputFile,'wb') as wfp:
            pickle.dump(dataset, wfp)
        with open(outputFile,'rb') as rfp:
            dataset = pickle.load(rfp)

    else :
        login_check()

login_check()