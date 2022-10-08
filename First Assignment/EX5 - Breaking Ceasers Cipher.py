# ----------------------------------------------------------------

# --> The idea : If we want to decrypt anf find the secret cipher of the tect given, we'd have to first find the key.
# In this case, we're not given the KEY, so we'd have to either : frequency analyse the text OR brute force through the options.

# ---------------

# In this matter, this code will present the brute force way :
# ==> Algorithm:
# 1 - input text
# 2 - decrypt the text with trying all keys ( from 1 to 25 )
# 3 - Once all 25 decrypted text has been revealed, there will be a question for the user to choose the most english texted from all the options



import string


def encrypt(key, message):
    message = message.upper()

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:

        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)
            result = result + alpha[letter_index]

        else:
            result = result + letter

    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:

        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]

        else:
            result = result + letter

    return result

def break_cipher(text):
    """ when the shift is unknown """
    for n in range(26):
        print(f"Using a shift value of {n}")
        print(decrypt(n, text))
        print("------------------")



user_input = "IFMMP"
break_cipher(user_input)
correct = input("Which of the following keys looks correct? ")
print("The correct ceaser cipher is ==> " + decrypt(int(correct),user_input) )
