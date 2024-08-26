# Caesar Cipher Project

This project is part of my internship at PRODIGYINFOTECH, where I am focusing on Cyber Security and Ethical Hacking. As a part of my learning experience, I developed a Python program to implement the Caesar Cipher encryption algorithm. This project showcases my understanding of fundamental cryptography techniques and my ability to write secure, efficient code.

## About the Internship

As I embark on my internship at Prodigy InfoTech, I am excited to dive into the world of cybersecurity and ethical hacking. This initial phase of my internship is focused on gaining practical experience in identifying vulnerabilities, securing systems, and learning about encryption and data protection. I look forward to applying my knowledge to real-world challenges and growing my skills in this dynamic field.



## Project Overview

The **Caesar Cipher** is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet. This Python script allows users to both encrypt and decrypt messages using a specified shift value.

### Features

- **Encryption and Decryption**: Encrypts and decrypts text using the Caesar Cipher method.
- **Shift Customization**: Allows users to specify the number of positions each letter should be shifted.
- **Handles Uppercase and Lowercase**: The script can handle both uppercase and lowercase letters appropriately.
- **Non-Alphabet Characters**: Non-alphabet characters remain unchanged, preserving spaces and punctuation.

## How to Use

1. **Clone the Repository**: Download or clone this repository to your local machine.
2. **Run the Script**: Execute the Python script using the command `python caesar_cipher.py` in your terminal or command prompt.
3. **Follow the Prompts**: Enter the message you wish to encrypt or decrypt and the desired shift value.

## Code

Here is the Python code for the Caesar Cipher:

```python
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
```

## Examples

### Example 1: Basic Encryption with Shift of 3

- **Input**:
  - Message: `HELLO`
  - Shift: `3`
- **Expected Output**: `KHOOR`

### Example 2: Handling Lowercase and Uppercase Letters

- **Input**:
  - Message: `Hello World`
  - Shift: `5`
- **Expected Output**: `Mjqqt Btwqi`

### Example 3: Wrapping Around the Alphabet

- **Input**:
  - Message: `XYZ`
  - Shift: `4`
- **Expected Output**: `BCD`

### Example 4: Encrypting with Special Characters

- **Input**:
  - Message: `Hello, World!`
  - Shift: `3`
- **Expected Output**: `Khoor, Zruog!`

### Example 5: Decrypting with the Same Shift Value

- **Input**:
  - Message: `Khoor`
  - Shift: `3`
  - Mode: Decrypt
- **Expected Output**: `Hello`

### Example 6: Using a Larger Shift

- **Input**:
  - Message: `PYTHON`
  - Shift: `10`
- **Expected Output**: `ZIDRYX`

## How to Run

To run this script, follow these steps:

1. Save the Python code to a file named `caesar_cipher.py`.
2. Open a command prompt and navigate to the directory where your file is saved.
3. Run the script by typing `python caesar_cipher.py` and follow the prompts.

Feel free to try different messages and shift values!
