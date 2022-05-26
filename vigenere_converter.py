US_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def decrypt_vigenere(file_name: str, key: str) -> str:
    
    # Read file
    with open(file_name, encoding="UTF-8") as file:
        encrypted_message = file.read()

    # Cleaning message to expand key
    cls_enc_message = [symbol for symbol in encrypted_message if symbol.isalpha()]
    cls_enc_message = "".join(cls_enc_message)
    
    # Expanding key
    expanded_key = key * int((len(cls_enc_message) / len(key)) + 1)

    while len(expanded_key) > len(cls_enc_message):
        expanded_key = expanded_key[:-1]

    # Decryption
    decrypted_message = ""
    iter_expanded_key = iter(expanded_key)
    for enc_symbol in encrypted_message:
        if enc_symbol.isalpha():
            key_symbol = next(iter_expanded_key)
            dec_symbol_index = (US_LETTERS.index(enc_symbol) - US_LETTERS.index(key_symbol)) % 26
            dec_symbol = US_LETTERS[dec_symbol_index]

        else: dec_symbol = enc_symbol
        decrypted_message += dec_symbol
    
    return decrypted_message


def main() -> None:
    file_name = input("Enter file name: ")
    key = "love"

    decrypted_message = decrypt_vigenere(file_name, key)

    # Writing message to the file
    with open(f"decrypted_{file_name}", mode="w", encoding="UTF-8") as file:
        file.write(decrypted_message)

    print("\n DECRYPTED MESSAGE: \n")
    print(decrypted_message)


main()