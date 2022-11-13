import rsa
import os
import sys

if int(len(sys.argv))>1:
	args=str(sys.argv[1])

paths='./'

#read my key
with open("seckey.pem","rb") as mykey:
	private_key=(rsa.PrivateKey.load_pkcs1(mykey.read().decode('utf8')) )

files=[]


if int(len(sys.argv))>1 and args=='current':
	for i in os.listdir():
		if i=='mal.py' or i=='seckey.pem' or i=='dec.py' or i=='reqs.txt':
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

print("Enter Layer.......................")
print("##################################")

Layer="sreesav"

user_input=input()

if user_input==Layer:
	print("List OF Files...")
	print(files)

	print("##############To encrypt all files write all or for specefic one enter file name###############")
	user_input=input()
	if user_input!='all':
		with open(paths+str(user_input),"rb") as targets:
				contents=targets.read()
		with open(paths+str(user_input),"w") as target:
				target.write(rsa.decrypt(contents, private_key).decode())
		print("DECRYPTED...............##################.....................")
		os.remove('./seckey.pem')

	elif files and user_input=='all':
		for i in files:
			with open(paths+str(i),"rb") as targets:
				contents=targets.read()
			with open(paths+str(i),"w") as target:
				target.write(rsa.decrypt(contents, private_key).decode())
		print("DECRYPTED...............##################.....................")
		os.remove('./seckey.pem')

	else:
		print("#######----No Files")
else:
	print("Failed................####################...................")