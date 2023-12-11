import hashlib

## runs through all the passwords in passlist to find a match
def crackHash(inputPass):
    try:
        passFile = open("passlist.txt", "r")
    except:
        print("could not find file.")

## looks through list
    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            print("password found: " + password)

##sets hash
if __name__ == '__main__':
    crackHash("1a1dc91c987325c69271ddf0c944bc72")

## code was made with the help of stackoverflow
