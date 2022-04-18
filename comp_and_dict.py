import hashlib

def bruteforce(passwordHashes, hashtype):

    wordlist = []
    wordfilename = "wordlist1.txt"
    wordfile = open(wordfilename, "r")
    print("Processing words...")
    for word in wordfile:
        wordlist.append(word.rstrip('\n'))
    wordfile.close()
    print("Words processed!")

    passwords = []
    suffixlist = ["01","02","03","04","05","06","07","08","09","!","@","#","$","%","^","&","*","?","=","/"]
    for year in range(1990, 2021):
        suffixlist.append(str(year))
    for year in range(90, 100):
        suffixlist.append(str(year))
    for year in range(1,21):
        suffixlist.append(str(year))
    wordlistHash=''
    passwordHash=passwordHashes
    iters=0

    while len(passwords) != 10:
        for w in wordlist:
            for suffix in suffixlist:
                for i in range(1, 9):
                    if i == 1:
                        word = w.capitalize()
                    elif i == 2:
                        word = w[:-1] + w[-1].upper()
                    elif i == 3:
                        word = w[:-1] + w[-1].upper() + suffix
                    elif i == 4:
                        word = suffix + w[:-1] + w[-1].upper()
                    elif i == 5:
                        word = suffix + w.capitalize()
                    elif i == 6:
                        word = w.capitalize() + suffix
                    elif i == 7:
                        word = w + suffix
                    elif i == 8:
                        word = suffix + w
               
                
                
                    if hashtype == 'sha1':
                        wordlistHash = hashlib.sha1(word.encode('utf-8')).hexdigest()
                        #print(f"Trying password: {word}:{wordlistHash}")
                        if wordlistHash == passwordHash[0]:
                            print(f"Found password 1: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[1]:
                            print(f"Found password 2: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[2]:
                            print(f"Found password 3: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[3]:
                            print(f"Found password 4: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[4]:
                            print(f"Found password 5: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[5]:
                            print(f"Found password 6: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[6]:
                            print(f"Found password 7: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[7]:
                            print(f"Found password 8: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[8]:
                            print(f"Found password 9: {word}")
                            passwords.append([word, hash])
                        if wordlistHash == passwordHash[9]:
                            print(f"Found password 10: {word}")
                            passwords.append([word, hash])
                        if iters % 1000000000 == 0:
                            print(iters, word)
                        iters+=1


hashlist = []

def hashesintolist(filename, hashlist):
    hashes = open(filename, "r")
    for hash in hashes:
        hashlist.append(hash.rstrip('\n'))
    hashes.close()
    return hashlist

hashlist = hashesintolist("comprehensive8", hashlist)
hashlist = hashesintolist("dictionary8", hashlist)
bruteforce(hashlist, 'sha1')
