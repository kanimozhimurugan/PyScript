"""
Create a new randomly generated password
"""
import string, random
characters = map(str, string.ascii_letters + string.digits)
def new(pin=9):
    return ''.join(random.choice(characters) for x in range(pin))



