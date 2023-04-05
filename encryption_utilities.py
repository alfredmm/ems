import csv

#Caesar cipher encrytion
def passwordEncrypt(unencryptedMessage, key):
    #We will start with an empty string as our encrypted message
    encryptedMessage = ""
    
    for symbol in encryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.lower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol
    return encryptedMessage

def loadPasswordFile(fileName):
    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)
    return passwordList

def savePasswordFile(passwordList, fileName):
    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)
                    