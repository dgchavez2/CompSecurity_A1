#!usr/bin/env/python3 

#from passlib.has import md5_crypt
import hashlib

f = open("shadowfile.txt", "r")
shadow_file = f.read()
f.close()

f1 = open("commonPasswdFile.txt", "r")
passwd_f1 = f1.read()
f1.close()

f2 = open("commonPasswdFile2.txt", "r")
passwd_f2 = f2.read()
f2.close()

hash_pass = []
cur = 0
for line in passwd_f1:
	hash_pass.append(hashlib.md5(line.encode('utf8')).hexdigest())
	print(hash_pass[cur])
	cur += 1
	

for line in shadow_file:
	shadow_line = line.split(":")[1]
	username = shadow_line[0]
	shadow_line = shadow_line.split("$")
	shadow_salt = shadow_line[1]
	shadow_passwd = shadow_line[2]

