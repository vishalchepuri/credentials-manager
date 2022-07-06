import cryptocode
import myencryption

def encrypt(data,paswd):
    var = cryptocode.encrypt(data,paswd)
    return var


def decrypt(data,paswd):
    var = cryptocode.decrypt(data,paswd)
    return var
