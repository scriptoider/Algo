import hashlib
import random
import string

class Password:

    def generatePassword(self, n1):
        password = random.choices(string.ascii_letters + string.digits + string.punctuation, k=n1-4)
        password += random.choices(string.ascii_lowercase)
        password += random.choices(string.digits)
        password += random.choices(string.punctuation)
        random.shuffle(password)
        password = ''.join(i for i in password)
        sha256 = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        md5 = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
        return (
            f"Password: {password}\n" +
            f"SHA256: {sha256}\n" +
            f"MD5: {md5}"
        )

    def checkPassword(self, password):
        if len(password) < 8:
            return 'Unsecure'
        cU = cL = cD = cS = 0
        for i in password:
            if i in string.ascii_uppercase:
                cU += 1
            elif i in string.ascii_lowercase:
                cL += 1
            elif i in string.digits:
                cD += 1
            elif i in string.punctuation:
                cS += 1
        if cU == 0 or cL == 0 or cD == 0 or cS == 0:
            return 'Unsecure'
        return 'Secure'
