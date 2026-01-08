alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def exit_program():
    user_exit = input("Exit Program? (Y/N): ").lower()
    if user_exit == "y":
        return False
    return True

def encrypt(original_text, shift_amount):
    print(f"Original Text: {original_text}")

    shifted_text = ""

    for char in original_text:
        if char in alphabet:
            original_text_index = alphabet.index(char)
            shifted_letter_index = original_text_index + shift_amount
            shifted_letter = alphabet[shifted_letter_index % len(alphabet)]
            shifted_text += shifted_letter

    print(f"Here is the encoded result: {shifted_text}")






def main():
    running = True
    while running:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n").lower()
        if direction == "exit":
            running = exit_program()
            continue

        if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(original_text = text, shift_amount = shift)

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


main()