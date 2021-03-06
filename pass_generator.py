# !/usr/bin/env python3
#
# This script will generate for you a cool password
# Author: OzoNeTT
# Github: https://github.com/OzoNeTT/SimplePasswordGenerator/

import base64
import hashlib
import random
import string as chars
from optparse import OptionParser

LETTERS = chars.ascii_letters
NUMBERS = chars.digits
PUNCTUATION = chars.punctuation
BANNED = '6bc(gq9CGLIil1|Oo0Ss5VUZ2zvu'


def create_shuffle(digits, letters, symbols, upper, lower):
    string_constant = ''

    string_constant += NUMBERS if digits else ''
    string_constant += PUNCTUATION if symbols else ''
    if letters:
        string_constant += LETTERS if not upper and not lower else LETTERS.lower()\
                           if lower else LETTERS.upper() if upper else ''

    return string_constant


def create_shuffle_ld(digits, letters, symbols, upper, lower):
    string_letters = ''

    if letters:
        string_letters = LETTERS if not upper and not lower else LETTERS.lower()\
                         if lower else LETTERS.upper() if upper else ''
    string_else = ''
    string_else += NUMBERS if digits else ''
    string_else += PUNCTUATION if symbols else ''
    return string_letters, string_else


def password_generator(length=16, digits=True, letters=True, symbols=True, upper=False,
                       lower=False, ld=False, uniq=False):
    random_password = ''
    if ld:
        printable_letters, printable_else = create_shuffle_ld(digits, letters, symbols, upper, lower)

        printable_letters = ''.join(c for c in printable_letters if c not in BANNED) if uniq else printable_letters
        printable_else = ''.join(c for c in printable_else if c not in BANNED) if uniq else printable_else

        printable_letters = list(printable_letters)
        printable_else = list(printable_else)

        random.shuffle(printable_letters)
        random.shuffle(printable_else)

        random_number = random.randint(1, length)
        last_number = length - random_number

        random_password_part_one = random.choices(printable_letters, k=random_number)
        random_password_part_two = random.choices(printable_else, k=last_number)

        random_password = ''.join(random_password_part_one) + ''.join(random_password_part_two)

    else:
        printable = create_shuffle(digits, letters, symbols, upper, lower)
        printable = ''.join(c for c in printable if c not in BANNED) if uniq else printable

        printable = list(printable)
        random.shuffle(printable)
        random_password = random.choices(printable, k=length)

        random_password = ''.join(random_password)
    return random_password


def save_to_file(string, filepath, username='', url='', b64_string='', md5_string=''):
    file = open(filepath, 'w')
    STRING = f'---------------------CREDENTIALS---------------------\n'
    STRING += f'URL:\t\t{url}\n' if url != '' else ''
    STRING += f'Username:\t{username}\n' if username != '' else ''
    STRING += f'Password:\t{string}\n'
    STRING += f'Base64:\t{b64_string}\n' if b64_string != '' else ''
    STRING += f'MD5:\t\t{md5_string}\n' if md5_string != '' else ''
    STRING += f'-----------------------------------------------------\n'

    file.write(STRING)
    file.close()


def printer(string, b64_string='', md5_string=''):
    outstring = f'{bcolors.HEADER}{art}{bcolors.TEXT}'
    outstring += f'Program finished successful, result:'
    outstring += f'\n\n{bcolors.PASS}Password: {string}'
    outstring += f'\nIn Base64: {b64_string}' if b64_string != '' else ''
    outstring += f'\nIn MD5: {md5_string}' if md5_string != '' else ''
    outstring += f'\n\n{bcolors.TEXT}Good luck!'
    return outstring


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

./pass_generator.py -l 25 -s --ld --md5 --base64

[+]result:

Program finished successful, result:                                                                                                                                                                                                       
                                                                                                                                                                                                                                           
Password: odmuectYpbEncBP3473548261                                                                                                                                                                                                        
In Base64: b2RtdWVjdFlwYkVuY0JQMzQ3MzU0ODI2MQ==                                                                                                                                                                                            
In MD5: 5873b555538590633e69652f728268f6                                                                                                                                                                                                   
                                                                                                                                                                                                                                           
Good luck! 
"""


def parser():
    parse = OptionParser(bcolors.HEADER + art + help_menu + bcolors.ENDC)

    parse.add_option("-l", "--len", dest="Length", type="string", help="Specify password length")
    parse.add_option("-u", "--url", dest="URL", type="string",
                     help="Set the website URL (optional for file output)")
    parse.add_option("-n", "--name", dest="Username", type="string",
                     help="Specify the username (optional for file output)")
    parse.add_option("-o", "--out", dest="File", type="string",
                     help="Output file. If it exists it will be overwrited!")
    parse.add_option("-P", dest="P", action='store_false', help="Do not use punctuation symbols")
    parse.add_option("-L", dest="L", action='store_false', help="Do not use letters")
    parse.add_option("-D", dest="D", action='store_false', help="Do not use digits")
    parse.add_option("-A", dest="A", action='store_true', help="The first letter of the password is capitalized")
    parse.add_option("-U", dest="Similar", action='store_true', help="Exclude Similar Characters")
    parse.add_option("--uce", dest="Upper", action='store_false', help="Use only upper case letters")
    parse.add_option("--lce", dest="Lower", action='store_false', help="Use only lower case letters")
    parse.add_option("--lf", dest="LD", action='store_false', help="Letters first")
    parse.add_option("--base64", dest="BASE64", action='store_true', help="Encrypt your password with base64")
    parse.add_option("--md5", dest="MD5", action='store_true', help="Encrypt your password with MD5")
    return parse.parse_args()


def opt_is_none(opt):
    return opt.Length is None and opt.URL is None and opt.Username is None and opt.File is None and opt.Upper is None \
           and opt.BASE64 is None and opt.P is None and opt.L is None and opt.D is None and opt.Similar is None \
           and opt.Lower is None and opt.LD is None and opt.MD5 is None and opt.A is None


def main_core():
    # Parse arguments
    (opt, args) = parser()

    # If program called without arguments
    if opt_is_none(opt):
        password = password_generator()
        print(printer(password))
        exit(0)

    LENGTH = 16
    try:
        LENGTH = int(opt.Length) if opt.Length is not None else 16
    except Exception:
        print(f'{bcolors.HEADER}{art}{bcolors.ENDC}Error error, as always! Type  -h  for help\n\n')
        exit(0)

    DIGITS = True if opt.D is None else False
    LETTER_CHARS = True if opt.L is None else False
    PUNCTUATION_SYMBOLS = True if opt.P is None else False

    if not PUNCTUATION_SYMBOLS and not DIGITS and not LETTER_CHARS:
        print(f'{bcolors.HEADER}{art}Sorry, you disabled everything, here is you password:\n\n'
              f'{bcolors.PASS}DuNkEy!\n\n{bcolors.TEXT}Good luck!')
        exit(0)

    UPPER_FLAG = False if opt.Upper is None else True
    LOWER_FLAG = False if opt.Lower is None else True
    LETTERS_FIRST = False if opt.LD is None else True
    UNIQ_CHARS = True if opt.Similar is not None else False

    if UPPER_FLAG and LOWER_FLAG:
        print(f'{bcolors.HEADER}{art}{bcolors.ENDC}ERROR 418, i am not a teapot!\n\n')
        exit(0)

    string = password_generator(length=LENGTH, digits=DIGITS, letters=LETTER_CHARS, symbols=PUNCTUATION_SYMBOLS,
                                upper=UPPER_FLAG, lower=LOWER_FLAG, ld=LETTERS_FIRST, uniq=UNIQ_CHARS)

    # Capitalize
    string = string.capitalize() if opt.A else string

    # Encryption
    b64_string = base64.b64encode(string.encode()).decode() if opt.BASE64 else ''
    md5_string = hashlib.md5(string.encode()).hexdigest() if opt.MD5 else ''

    # if password will be written into file
    if opt.File is not None:
        FILEPATH = str(opt.File)
        URL = str(opt.URL) if opt.URL is not None else ''
        USERNAME = str(opt.Username) if opt.Username is not None else ''
        save_to_file(string, FILEPATH, username=USERNAME, url=URL, b64_string=b64_string, md5_string=md5_string)
        exit(0)

    # Main print
    print(printer(string, b64_string=b64_string, md5_string=md5_string))
    exit(0)


if __name__ == "__main__":
    main_core()
    exit(0)
