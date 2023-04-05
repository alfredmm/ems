import sys
from encryption_utilities import loadPasswordFile, savePasswordFile, passwordEncrypt
#The password list - we start with it populated for testing purposes
passwords = [['yahoo', 'XqffoZeo'],['google', 'CoIushujSetu']]

#The password file to store passwords to
passwordFileName = 'samplePasswordFile'

#The Encryption key for caesar cipher
encryptionKey = 16

while True:
    print("What would you like to do?")
    print("1. Open Password File")
    print("2. Lookup a Password")
    print("3. Add a Password")
    print("4. Save Password File")
    print("5. Print Encrypted Password List (for Testing)")
    print("6. Quit Program")
    print("Please enter number (1-4)")

    choice = input()

    if choice == '1': #Load the password list from file
        passwords = loadPasswordFile(passwordFileName)
    if choice == '2': #Look up a password
        print("Which website do you want to look the password for") 
        passwords = loadPasswordFile(passwordFileName)

        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        ###CODE HERE###
        #1. Loop through passwords list
        for record in passwords:
            site = record[0]
            encrypted_password = record[1]
            decrypted_pass = decrypt_password(encrypted_password, encryptionKey)
            print(f"Password for {site}: {decrypted_pass}")        

        #2. Check if name is found        #3. If name is found, decrypt
        def decrypt_password(encrypted_password, key):
            decrypted_pass = ""
            for character in encrypted_password:
                if character.isalpha():
                    shifted_character = chr((ord(character.lower()) - 97 - key) % 26 + 97)
                    if character.isupper():
                        shifted_character = shifted_character.upper()
                    decrypted_pass += shifted_character
                else:
                    decrypted_pass += character
            return decrypted_pass
    
    if choice == '3':
        print("Which website do you want to encrypt the password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

         #####CODE HERE###
        #Encrypt the password and store it in the list of passwords
        #Step 1: Encrypt ---- encryptedPassword  = passwordEncrypt(unencryptedPassword, encryptionKey)
        encryptedPass = passwordEncrypt(unencryptedPassword, encryptionKey)
        #Step 2: Create list of size 2 [website name, password]
        new_passwords = [None, None]
        #Step 3: Append list from step 2 to password list
        new_passwords.insert(0, website)
        new_passwords.insert(1,encryptedPass)
        passwords.append(new_passwords)

    if choice == '4': #save passwords to file
        savePasswordFile(passwords, passwordFileName) 
    
    if choice == '5': # print password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if choice == '6': #Exit program
        sys.exit()
    
    print("Passwords: ", passwords)
    print()

