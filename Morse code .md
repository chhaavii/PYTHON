

# Morse Code Encoder and Decoder

## Description
This Python program allows you to encode regular text into a custom Morse code format and decode Morse code back to normal text. It uses a unique mapping between alphabet letters and numbers to Morse code characters, providing a simple way to conceal text messages.

## Features
- **Encoding**: Convert a given message into Morse code using a pre-defined mapping.
- **Decoding**: Convert Morse code back into the original message.
- **Special Character Handling**: Keeps spaces and special characters (`.,;[]{}*!@#%^&()` etc.) intact during encoding and decoding.
- **Error Handling**: Unsupported characters are replaced with `?` in both encoding and decoding.

## Requirements
- Python 3.x

## Installation
1. Clone or download the repository.

## Usage
1. Run the script:
   ```bash
   python morse_code.py
   ```
2. Follow the on-screen prompts:
   - Choose `1` to encode text into Morse code.
   - Choose `2` to decode Morse code back to text.
3. Input your message, and the program will display the result.
4. After each operation, you can continue encoding or decoding by selecting `1` or `2` or exit by entering any other number.

## Example
### Encoding
```
What do you wish to do?
1. Encode your words to Morse
2. Decode Morse to normal text
Your answer: 1
Enter the text you want to encode: HELLO
Encoded to Morse: vntt*
```

### Decoding
```
What do you wish to do?
1. Encode your words to Morse
2. Decode Morse to normal text
Your answer: 2
Enter the Morse code you want to decode: vntt*
Decoded to normal text: HELLO
```

## Key Mapping
The program uses the following mapping between text characters and Morse code:
- **Alphabet**: Each letter from A-Z has a corresponding Morse character. 
  - Example: `A` maps to `f`, `B` to `j`, etc.
- **Numbers**: 0-9 are also mapped to Morse characters.
  - Example: `0` maps to `9`, `1` to `7`, etc.
- **Special Characters**: Preserved in the text and remain the same after encoding/decoding.

## License
This project is open-source and available under the MIT License.

--- 

This README should help users understand the functionality and usage of the program. Adjust the details if you add more features or make any changes to the code!
