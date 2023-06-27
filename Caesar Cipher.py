Alphabates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Typr the message:\n").lower()
shift = int(input("Type the shift number:\n"))




def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = Alphabates.index(letter)
        new_position = position + shift_amount
        new_letter = Alphabates[new_position]
        cipher_text += new_letter
    print(f"Ther encoded text is {cipher_text}")
    



def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = Alphabates.index(letter)
        new_position = position - shift_amount
        new_letter = Alphabates[new_position]
        plain_text += new_letter
    print(f"Ther decoded text is {plain_text}")
    



if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text,shift_amount=shift)
    