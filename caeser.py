def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift if mode == 'encrypt' else -shift

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode: (e)ncrypt or (d)ecrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if mode == 'e':
        output = caesar_cipher(message, shift, 'encrypt')
    elif mode == 'd':
        output = caesar_cipher(message, shift, 'decrypt')
    else:
        print("Invalid mode selected.")
        return

    print(f"Result: {output}")


if __name__ == "__main__":
    main()
