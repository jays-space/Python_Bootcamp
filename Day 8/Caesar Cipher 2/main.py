alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def exit_program():
    user_exit = input("Exit Program? (Y/N): ").lower()
    if user_exit == "y":
        return False
    return True

# def encrypt(original_text, shift_amount):
#     shifted_text = ""
#
#     for char in original_text:
#         if char in alphabet:
#             original_text_index = alphabet.index(char)
#             shifted_letter_index = original_text_index + shift_amount
#             shifted_letter = alphabet[shifted_letter_index % len(alphabet)]
#             shifted_text += shifted_letter
#
#     print(f"Here is the encoded result: {shifted_text}")
#
# def decrypt(original_text, shift_amount):
#     shifted_text = ""
#
#     for char in original_text:
#         if char in alphabet:
#             original_text_index = alphabet.index(char)
#             shifted_letter_index = original_text_index - shift_amount
#             shifted_letter = alphabet[shifted_letter_index % len(alphabet)]
#             shifted_text += shifted_letter
#
#     print(f"Here is the decoded result: {shifted_text}")

def cypher(original_text, shift_amount, direction):
    shifted_text = ""

    for char in original_text:
        if char in alphabet:
            original_text_index = alphabet.index(char)
            shifted_letter_index = original_text_index + shift_amount if direction == "encode" else original_text_index - shift_amount
            shifted_letter = alphabet[shifted_letter_index % len(alphabet)]
            shifted_text += shifted_letter

    print(f"Here is the {direction}d result: {shifted_text}")

def main():
    running = True
    while running:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n").lower()
        if direction == "exit":
            running = exit_program()
            continue

        # if direction == "encode":
        #     text = input("Type your message:\n").lower()
        #     shift = int(input("Type the shift number:\n"))
        #     encrypt(original_text = text, shift_amount = shift)
        #
        # if direction == "decode":
        #     text = input("Type your encrypted message:\n").lower()
        #     shift = int(input("Type the shift number:\n"))
        #     decrypt(original_text = text, shift_amount = shift)

        if direction == "encode" or direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            cypher(original_text = text, shift_amount = shift, direction = direction)

main()


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.