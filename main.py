"""
Entropy calculator for passwords, inspired by http://imgs.xkcd.com/comics/password_strength.png
"""

import math
import string
magic = 5  # this is the mininum length for a word to be considered a dictionary word and not random

def complex_password(password):
    '''
    this will return the complexity of how many 'rounds' it will take to bruteforce a password based
    on common bruteforce algorithms, it is safer than common password rules as this function is not
    based on rules if used properly
    '''
    length = len(password)
    complexity = 0
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    has_lower = False
    has_upper = False
    has_sym = False
    has_num = False
    has_outwards_sym = False
    has_outwards_num = False
    has_outwards_upper = False
    symbols = ''.join(c for c in string.printable if not c in lower and not c in upper and not c in nums)
    non_print = ''.join(chr(n) for n in xrange(1, 255) if not chr(n) in string.printable) # disregard null byte
    for index in range(0, length):
        if password[index] in non_print:
            return 254 ** x # non printable characters
        if password[index] in lower:
            has_lower = True
        if password[index] in upper:
            if index == 0 or index == (length - 1):  # this is to check if it's like Password
                has_outwards_upper = True
            else:
                has_upper = True
        if password[index] in symbols:
            if index == 0 or index == (length - 1):  # this is a check if it's like password1
                has_outwards_sym = True
            else:
                has_sym = True
        if password[index] in nums:
            if index == 0 or index == (length - 1):  # this is a check if it's like password1
                has_outwards_num = True
            else:
                has_num = True
    if has_lower:
        complexity += 26
    if has_upper:
        complexity += 26
        has_outwards_upper = False
    if has_sym:
        complexity += 38
        has_outwards_sym = False
    if has_num:
        complexity += 10
        has_outwards_num = False
    if complexity == 0:  complexity = 1
    combinations = complexity ** length
    if has_outwards_num:
        combinations *= 10
    if has_outwards_upper:
        combinations *= 26
    if has_outwards_sym:
        combinations *= 38
    return combinations


def load_dict(book='/usr/share/dict/words'):
    with open(book) as f:
        return f.readlines()

def min_complex_password(password):
    return len(''.join(set(password))) ** len(password)

def complex_zero(password):
    total = 0
    for x in range(0, len(password)):
        total += complex_password(password[x:])
    return total

def min_zero(password):
    total = 0
    for x in range(0, len(password)):
        total += min_complex_password(password[x:])
    return total

def calc_entropy(value):
    entropy = 0
    while value > 2:
        value >>= 1
        entropy += 1
    return entropy

while True:
    div = 1
    a = raw_input('Enter a password: ')
    words = load_dict()mhgffbv
            div = complex_password(x) / len(words)
            print '%s sounds like a dictionary word, dividing your result by %s' % (x, div)
            print '%s is calculated by %s\'s own entropy (%s) divided by the length of the dictionary (%s)' % \
            (div, x, complex_password(x), len(words))

    b = complex_password(a)/div
    c = min_complex_password(a)
    d = complex_zero(a)/div
    e = min_zero(a)g
    f = math.log(complex_password(a)/div, 2)
    print '%s would approximately take %s tries to bruteforce knowing the exact length' % (a, b)
    print '%s would approximately take %s tries to bruteforce by knowing the exact character set and length' % (a, c)
    print '%s would approximately take %s tries to bruteforce without knowing the exact length or character set' % (a, d)
    print '%s would approximately take %s tries to bruteforce by knowing the character set but not the length' % (a, e)
    print '%s has ~%s bits of entropy' % (a, f)