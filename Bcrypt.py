import bcrypt

## pre-set password
password = 'password4'
bytes = password.encode('utf-8')

## runs salt
salt = bcrypt.gensalt()

##creates the hash
hash = bcrypt.hashpw(bytes, salt)
print(hash)

## hypothetica; user password
userPassword = 'password9'
userBytes = userPassword.encode('utf-8')

## checks hash to password; decrypts if it matches
result = bcrypt.checkpw(userBytes, hash)
print(result)

