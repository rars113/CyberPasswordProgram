import hashlib
import itertools

##iterates through chars a-z 1-9
def bruteforce(hash):
    letters = [chr(n) for n in range(ord('A'), ord ('z'))]
    digits = [chr(n) for n in range(ord('0'), ord('9'))]

    ##nested for-loop to form hash
    for part1 in itertools.product(letters, repeat = 3):
        for part2 in itertools.product(digits, repeat = 4):
            passowrdTry = ''.join(part1 + part2) ##joins both to make an attempt
            if hashlib.sha256(passowrdTry.encode()).hexdigest() == hash:
                return passowrdTry
 ##pre-set test           
testPassword = "BOO8000"
##tests against hash
key = hashlib.sha256(testPassword.encode()).hexdigest()
print("Hash: %s" % key)
print("Brute-forcing...")
##brutes through everything
recoveredKey = bruteforce(key)
print("brute force result: %s" % recoveredKey)
