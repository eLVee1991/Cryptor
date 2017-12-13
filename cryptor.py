from simplecrypt import encrypt, decrypt
from os.path import exists
from os import unlink
from messageColor import message
import getpass
import string
import random

randomKey = "gen.enc"
fileName =  "keys.enc"

def stringGen(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def randomKeyFile(file_name):
	with open(file_name, "w") as kfile:
		key = stringGen(256)
		kfile.write(key)
		kfile.close()

def encryptor(file_name, key, plaintext):
	with open(file_name, 'w') as efile:
		enc = encrypt(key, plaintext)
		efile.write(enc)
		efile.close()

def decryptor(file_name, key):
	with open(file_name, 'rb') as dfile:
		ciphertext = dfile.read()
		dec = decrypt(key, ciphertext)
		message("info", "> '"+dec+"'"+" is the content of the encrypted file.")
		dfile.close()
		#return dec

def main():
	# read or create the file
	if exists(fileName) and exists(randomKey):
		message("succes", "[+] The password was found. It will now be used.")
		data = decryptor(fileName, randomKey)
	else:
		while True:
			message("warning", "[+] The password file cannot be found. Do you want to create it? y/n.")
			answer = raw_input("> ")
			if answer == "y" or answer == "Y":
				randomKeyFile(randomKey)
				keys = getpass.getpass()
				encryptor(fileName, randomKey, keys)
				message("succes", "[+] Succes! The password file has been created.")
				break
			elif answer == "n" or answer == "N":
				message("warning", "[+] Stopping the script.")
				exit()
			else:
				message("warning", "[+] Wrong input. Please enter y/n.")

if __name__ == "__main__":
	main()

	
