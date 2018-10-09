#!/usr/bin/env python
import passlib.hash
import sys
from datetime import datetime

# Define variables
# counter to keep track of how many passwords were cracked
# hashList list to store hashes from file that we found
counter = 0
hashList = []

# Open file that contains list of passwords
# I used rockyou.txt as the base file
# Just copied first 1068 words
try:
    with open('wordlist_full') as f:
        pwdList = f.read().split()

# Since the name of the file is hardcoded, we need to check if file exists, if not
# exception is handeled
except IOError:
    print("No such file or directory!")
    sys.exit()

# Open file that contains hashes
# and store hashes to the list hashList
try:
    with open('passwd') as f:
        hashFile = f.read().split()
        # Check what time the program started to crack passwords
        startTime = datetime.now()
        # Loop to split lines from hashFile
        # and to determine salt and username
        for line in hashFile:
            if line.strip():
                if "$" in line:
                    salt = line.split("$")[2]
                if ":" in line:
                    hashList.append(line.split(":")[-1])
                    username = line.split(":")[0]
                    # Loop to check each hashCode from the list
                    # and compare it to the hashcode of the word from wordlist
                    for hashCode in hashList:
                        for pwd in pwdList:
                                # Passlib function that returns the hash (apache md5_crypt) of word
                                # from wordlist with given salt
                            h = passlib.hash.apr_md5_crypt.encrypt(pwd, salt=salt)
                            if h == hashCode:
                                # Increase counter by 1 (number of cracked passwords)
                                counter += 1
                                # Print the message if password is found
                                print(('Collision!  The password for {}  is {}').format(username, pwd))

# Since the name of the file is hardcoded, we need to check if file exists, if not
# exception is handeled
except IOError:
    print("No such file or directory!")
    sys.exit()

# Checking the time again
endTime = datetime.now()

# Calc total time needed to finish pwd cracking
totalTime = endTime - startTime

# print the result
print('total time > ', totalTime)
print('number of password cracked > ', counter)
