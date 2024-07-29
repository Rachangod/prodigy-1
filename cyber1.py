def encrypt_caesar_cipher(text, shift):
    """
    Encrypts the given text using Caesar Cipher with the specified shift.
    
    :param text: The input text to be encrypted
    :param shift: The number of positions to shift each character
    :return: The encrypted text
    """
    encrypted_text = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt_caesar_cipher(text, shift):
    """
    Decrypts the given text using Caesar Cipher with the specified shift.
    
    :param text: The input text to be decrypted
    :param shift: The number of positions to shift each character
    :return: The decrypted text
    """
    return encrypt_caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Program")
    
    while True:
        mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter the text: ").strip()
        
        try:
            shift = int(input("Enter the shift value: ").strip())
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if mode == 'encrypt':
            result = encrypt_caesar_cipher(text, shift)
        elif mode == 'decrypt':
            result = decrypt_caesar_cipher(text, shift)

        print(f"Result: {result}")
        
        # Ask the user if they want to run another operation
        another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
