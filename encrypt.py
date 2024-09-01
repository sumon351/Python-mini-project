# encryption project using python
import random
import string
chars=" " + string.digits + string.punctuation + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
# print(f"chars : {chars}")
# print(f"key   : {key}")
#encrypt 
plain_text=input("Enter a message to encrypt : ")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"original message : {plain_text}")
print(f"encrypted message : {cipher_text}")

#decrypt 
cipher_text=input("enter a message to decrypt : ")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]
print(f"encypt message    : {cipher_text}")
print(f"decrypted message : {plain_text}")
