import random

def generatePassward(length = 12):
    if length < 12:
        raise Exception("The passward must be 12 character or more")
    
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    specialCharacters = "!@#$%^&*()-=+"

    allCharacters = lowercase_letters + uppercase_letters + numbers + specialCharacters

    Passward = [random.choice(lowercase_letters), random.choice(uppercase_letters), random.choice(numbers), random.choice(specialCharacters)]
    
    lengthDiff = length - len(Passward)

    Passward = Passward + random.choices(allCharacters , k= lengthDiff)
    return ''.join(Passward)
print(generatePassward(16))

