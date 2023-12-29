#!/usr/bin/env python3

import hashlib
import questionary

# define function to calculate the hash value of input obtained from user using 
# hashlib library
def calculate_hash(string, algorithm):
	hash_object = hashlib.new(algorithm)
	hash_object.update(string.encode('utf-8'))
	print (hash_object.hexdigest())


# define a main function to ask the user the string to hash and the hashing algorithm
# call calculate_hash function using input parameters and print results
def main():
	print ('''
---------------------
   Hash Calculator
---------------------
	''')

	string = input("Enter string to hash: ")

	choice = questionary.select(
		"Select a hashing algorithm:",
		choices=["MD5","SHA-224","SHA-256","SHA-512"]
	).ask()
	
	algorithm = ""
	
	if choice == "MD5":
		algorithm = "md5"
	elif choice == "SHA-224":
		algorithm = "sha224"
	elif choice == "SHA-256":
		algorithm = "sha256"
	else: algorithm = "sha512"
	
	calculate_hash(string, algorithm)
	
main()


