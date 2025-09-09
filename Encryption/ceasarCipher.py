
plaintext="ZEBRA"
key="H"

def caesar_encrypt(plaintext,key):
 shift=ord(key)-ord('A')
 cyphertext=""                   
 for letter in plaintext:
  if ord(letter)+ shift > ord('Z'):
   cyphertext+=chr(ord(letter)+shift-26)
  else:
   cyphertext+=chr(ord(letter)+shift)
 return cyphertext

def caesar_decrypt(cyphertext,key):
 shift=ord(key)-ord('A')
 plaintext=""                   
 for letter in cyphertext:
  if ord(letter) - shift < ord('A'):
   plaintext+=chr(ord(letter)-shift+26)
  else:
   plaintext+=chr(ord(letter)-shift)
 return plaintext

#print(caesar_encrypt(plaintext,key))

print(caesar_decrypt(caesar_encrypt(plaintext,key),key))
