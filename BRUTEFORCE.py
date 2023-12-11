import itertools
from ntpath import join
import string
import re
from symtable import Symbol
import time

User_Pass = ''

runTheServer = 1

def guessPass(real):
    passGen = string.ascii_letters + string.digits
    attempts = 0
    showTheGuess = input('Do you want to see the output? Will slwo down the process. (y/n) >> ').lower()
    startTime = time.time()

    for passwordLength in range(1,7):
        if showTheGuess == 'y':
            for guess in itertools.product(passGen, repeat=passwordLength):
                attempts +=1
                guess = ''.join(guess)
                if guess == real:
                    print('\n\nThe Pass has been found in ---- %s seconds ----' % (time.time() - startTime))
                    return f'\n Pass : {guess} | number of attempts : {attempts}'
                
                print(f'Pass {guess} | Number of attempts {attempts}')

        elif showTheGuess == 'n':
            attempts +=1
            guess = ''.join(guess)
            if guess == real:
                print('\n\nThe pass has been found in ---- %s seconds ----' % (time.time() - startTime))
                return f'\n pass is : {guess} | found in : {attempts} attempts'
        
        else:
            print('[-] Error ')
            break

while runTheServer == 1:
    while User_Pass != '......':
        User_Pass = input('\n\n[+] please enter a pass to be cracked\nMax 6 length\nOnly numbers and lowercase (Upper will convert to lower)\n >>>').lower()
        stringSet = set(User_Pass)
        punctuationSet = set(string.punctuation)

        if re.search(r'[\s]', User_Pass):
            print('[!] No spaces')
            time.sleep(1)
            continue
        elif stringSet.intersection(punctuationSet):
            print('[!] No no special char')
            time.sleep(1)
            continue
        elif len(User_Pass) > 6:
            print('[!] pass max length is 6')
            time.sleep(1)
            continue
        elif User_Pass == '':
            print('[!] password is null')
            time.sleep(1)
            continue
        else:
            ('\n[+] .. Starting .. \n')
            time.sleep(1)
            print(guessPass(User_Pass))
            print('--------')
            break
