# TODO-1: Import and print the logo from art.py when the program starts.
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?


def exit_program():
    user_exit = input("Exit Program? (Y/N): ").lower()
    if user_exit == "y":
        return False
    return True

def cypher(original_text, shift_amount, direction):
    shifted_text = ""
    const_alphabet = 26
    const_units = 10

    for char in original_text:
        ascii_val = ord(char)

        if 0 <= ascii_val <= 256:
            original_text_index = ascii_val
            shifted_letter_index = (original_text_index + shift_amount) if direction == "encode" else original_text_index - shift_amount
            shifted_letter = chr((shifted_letter_index % 256) + 0)
            shifted_text += shifted_letter

        # if char == ' ':
        #     original_text_index = ord(char) - ord(' ')
        #     shifted_letter_index = (original_text_index + shift_amount) if direction == "encode" else original_text_index - shift_amount
        #     shifted_letter = chr((shifted_letter_index % 1) + ord(' '))
        #     shifted_text += shifted_letter

        # if 'a' <= char <= 'z':
        #     original_text_index = ord(char) - ord('a')
        #     shifted_letter_index = (original_text_index + shift_amount) if direction == "encode" else original_text_index - shift_amount
        #     shifted_letter = chr((shifted_letter_index % const_alphabet) + ord('a'))
        #     shifted_text += shifted_letter
        #
        # if 'A' <= char <= 'Z':
        #     original_text_index = ord(char) - ord('A')
        #     shifted_letter_index = (original_text_index + shift_amount) if direction == "encode" else original_text_index - shift_amount
        #     shifted_letter = chr((shifted_letter_index % const_alphabet) + ord('A'))
        #     shifted_text += shifted_letter
        #
        # if '0' <= char <= '9':
        #     original_text_index = ord(char) - ord('0')
        #     shifted_letter_index = (original_text_index + shift_amount) if direction == "encode" else original_text_index - shift_amount
        #     shifted_letter = chr((shifted_letter_index % const_units) + ord('0'))
        #     shifted_text += shifted_letter



        # rrjjjjyy%rrjj%ffyy%:0uurr
        # 5
    print(f"Here is the {direction}d result: {shifted_text}")

def main():
    print(art.logo)
    print("Welcome to Caesar Cipher!")
    running = True

    while running:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n").lower()
        if direction == "exit":
            running = exit_program()
            continue

        if direction == "encode" or direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            cypher(original_text = text, shift_amount = shift, direction = direction)

main()