UA_LETTERS = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"

def decrypt_caeser(file_name: str) -> str:

    # Read file
    with open(file_name, encoding="UTF-8") as file:
        encrypted_message = file.read()

    # Calculate the most frequent letter 
    letters_frequency = {}
    for letter in encrypted_message:
        if letter.isalpha():
            letters_frequency[letter] = encrypted_message.count(letter) / len(
                encrypted_message
            )

    letters_frequency = {
        k: v for k, v in sorted(letters_frequency.items(), key=lambda v: v[1], reverse=True)
    }
    max_frqnc = list(letters_frequency.items())[0]


    # Calculating key for decryption
    key = abs(17 - UA_LETTERS.index(max_frqnc[0]))
    print(f"Encryption key was probably: {key}")

    # Decrypting
    decrypted_message = ""
    for encrypted_letter in encrypted_message:
        if encrypted_letter.isalpha():
            letter_index = UA_LETTERS.index(encrypted_letter) - key
            if letter_index < 0:
                letter_index += 1
            decrypted_letter = UA_LETTERS[letter_index]

        elif encrypted_letter.isnumeric():
            pass

        else:   
            decrypted_letter = encrypted_letter

        decrypted_message += decrypted_letter

    return decrypted_message

def main() -> None:
    file_name = input("Enter file name: ")

    decrypted_message = decrypt_caeser(file_name)

    # Writing message to the file
    with open(f"decrypted_{file_name}", mode="w", encoding="UTF-8") as file:
        file.write(decrypted_message)

    print("\n DECRYPTED MESSAGE: \n")
    print(decrypted_message)


main()