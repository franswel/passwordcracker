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
    key = 0
    wordlistHash=''
    passwordHash=passwordHashes
    iters=0

    while key == 0:
        for word in wordlist:
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
                #if iters % 10000 == 0:
                    #print(iters)
                #iters+=1
        key = 1

hashlist = []
filename = "basic8survey" # Change the name of the file here!!!!!!
hashes = open(filename, "r")
for hash in hashes:
    hashlist.append(hash.rstrip('\n'))
hashes.close()
bruteforce(hashlist, 'sha1')