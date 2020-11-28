# !/usr/bin/python3
#
# This script will generate for you a cool password
# Author: OzoNeTT
# Github: https://github.com/OzoNeTT/SimplePasswordGenerator/

import string as chars
import random
import base64
from optparse import OptionParser


LETTERS = chars.ascii_letters
NUMBERS = chars.digits
PUNCTUATION = chars.punctuation


def create_shuffle(digits, letters, symbols, lowercase=0):
    string_constant = ''

    # only lowercase WILL COME IN NEXT UPDATE
    if lowercase == 1:
        string_constant += NUMBERS if digits else ''
        string_constant += LETTERS.lower() if letters else ''
        string_constant += PUNCTUATION if symbols else ''
    # only uppercase
    elif lowercase == 2:
        string_constant += NUMBERS if digits else ''
        string_constant += LETTERS.upper() if letters else ''
        string_constant += PUNCTUATION if symbols else ''
    else:
        string_constant += NUMBERS if digits else ''
        string_constant += LETTERS if letters else ''
        string_constant += PUNCTUATION if symbols else ''

    return string_constant


def password_generator(length=8, digits=True, letters=True, symbols=True):
    printable = create_shuffle(digits, letters, symbols)

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password
    random_password = random.choices(printable, k=length)

    # convert generated password to string
    random_password = ''.join(random_password)
    return random_password


def save_to_file(string, filepath, username=None, url=None):
    file = open(filepath, 'w')
    if url is not None:
        if username is not None:
            file.write(f'---------------------CREDENTIALS---------------------\n'
                       f'URL:\t\t{url}\n'
                       f'Username:\t{username}\n'
                       f'Password:\t{string}\n'
                       f'-----------------------------------------------------\n')
        else:
            file.write(f'---------------------CREDENTIALS---------------------\n'
                       f'URL:\t\t{url}\n'
                       f'Password:\t{string}\n'
                       f'-----------------------------------------------------\n')
    else:
        if username is not None:
            file.write(f'---------------------CREDENTIALS---------------------\n'
                       f'Username:\t{username}\n'
                       f'Password:\t{string}\n'
                       f'-----------------------------------------------------\n')
        else:
            file.write(f'---------------------CREDENTIALS---------------------\n'
                       f'Password:\t{string}\n'
                       f'-----------------------------------------------------\n')
    file.write(string)
    file.close()


class bcolors:
    HEADER = '\033[36m'
    ENDC = '\033[31m'
    TEXT = '\033[32m'
    PASS = '\033[36m'


art = """
                /|  /|  ---------------------------
                ||__||  |                         |
               /   O O\__     Simple password     |
              /          \       generator        |
             /      \     \                       |
            /   _    \     \ ----------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \C_c_c_c


"""

help_menu = """ 

./pass_generator.py [options]

[+]usage: 

./pass_generator.py -l 12 -o file.txt -b
./pass_generator.py -n Username -u http://localhost/ -o file.txt -b

[+]result:

Your password is:

euisfh&T#f9(Wf,0gvfiudh

Good luck!

"""


def main_core():
    parse = OptionParser(bcolors.HEADER + art + help_menu + bcolors.ENDC)

    parse.add_option("-l", dest="L", type="string", help="Specify password length")
    parse.add_option("-u", dest="U", type="string", help="Set the website URL (optional for file output)")
    parse.add_option("-n", dest="N", type="string", help="Specify the username (optional for file output)")
    parse.add_option("-o", dest="O", type="string", help="Output file. If it exists it will be overwrited!")
    parse.add_option("-b", dest="B", action='store_false', help="Convert everything to base64")
    parse.add_option("-s", dest="S", action='store_true', help="Do not use punctuation symbols")
    parse.add_option("-c", dest="C", action='store_true', help="Do not use letters")
    parse.add_option("-d", dest="D", action='store_true', help="Do not use digits")

    (opt, args) = parse.parse_args()

    if opt.L is None and opt.U is None and opt.N is None and opt.O is None and opt.B is None and opt.S is None and \
            opt.C is None and opt.D is None:
        password = password_generator()
        print(f'{bcolors.TEXT}{art}Your password is:\n\n{bcolors.PASS}{password}\n\n{bcolors.TEXT}Good luck!')
        exit(0)

    string = ''
    LENGTH = int(opt.L) if opt.L is not None else 16
    PUNSYMBOLS = not opt.S
    DIGITS = not opt.D
    LETT = not opt.C

    if not PUNSYMBOLS and not DIGITS and not LETT:
        print(f'{bcolors.TEXT}{art}Sorry, you disabled everything, here is you password:\n\n'
              f'{bcolors.PASS}DuNkEy!\n\n{bcolors.TEXT}Good luck!')
        exit(0)

    string = password_generator(length=LENGTH, digits=DIGITS, letters=LETT, symbols=PUNSYMBOLS)

    if opt.B:
        string = base64.b32encode(string)

    # if file will be written into file
    if opt.O is not None:
        if opt.U is not None:
            if opt.N is not None:
                save_to_file(string, str(opt.O), username=str(opt.N), url=str(opt.U))
            else:
                save_to_file(string, str(opt.O), url=str(opt.U))
        else:
            if opt.N is not None:
                save_to_file(string, str(opt.O), username=str(opt.N))
            else:
                save_to_file(string, str(opt.O))
        exit(0)

    print(f'{bcolors.TEXT}{art}Your password is:\n\n{bcolors.PASS}{string}\n\n{bcolors.TEXT}Good luck!')
    exit(0)


if __name__ == "__main__":
    main_core()