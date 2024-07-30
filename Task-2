# My name is khaja masthan Shaik
# Task - 2

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#encryption function

def encrypt(message, key):
  encrypt = " "
  for data in message:
    if data.isalpha():
      position = alphabets.index(data)
      new_position = (position + key) % 26
      encrypt += alphabets[new_position]

  print(f"The encrypted message is: {encrypt}")

#decryption function 

def decryption(message, key):
  decrypt = " "
  for data in message:
    if data.isalpha():
      position = alphabets.index(data)
      new_position = (position - key) % 26
      decrypt += alphabets[new_position]

  print(f"The decrypted message is: {decrypt}")

print("                             Enter for encode for encryption or decode for decryption\n")

type = input("Enter for encode or decode:\n").strip()
message = input("Enter the message:\n").strip()
key = int(input("Enter the key:\n"))

if type == "encode":
  encrypt(message, key)
elif type == "decode":
  decryption(message, key)
else:
  print("Invalid input")
