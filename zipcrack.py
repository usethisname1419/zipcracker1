import zipfile
import itertools
import string


characters = string.ascii_letters + string.digits


zip_file = "ZIP.zip"

def try_password(password):

    try:
        with zipfile.ZipFile(zip_file, 'r') as zf:
            zf.extractall(pwd=password.encode())
        print(f"\nPassword cracked: {password}")
        return True
    except Exception as e:
        print(f"\rTrying password: {password}", end='')
        return False

def crack_zip():
    for length in range(4, 13):  # Range from 4 to 12 inclusive
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            if try_password(password):
                return

if __name__ == "__main__":
    crack_zip()
