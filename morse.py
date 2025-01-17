print("The program uses a specific key")
morse = {
    'A': 'f', 'B': 'j', 'C': 'b', 'D': 'k', 'E': 'n', 'F': 'q', 'G': 'l', 'H': 'v',
    'I': 'z', 'J': 'x', 'K': 'w', 'L': 't', 'M': 'e', 'N': 'a', 'O': 'r', 'P': 'c',
    'Q': 'g', 'R': 'm', 'S': 'o', 'T': 's', 'U': 'y', 'V': 'd', 'W': 'h', 'X': 'p',
    'Y': 'u', 'Z': 'i', '0': '9', '1': '7', '2': '5', '3': '8', '4': '1',
    '5': '6', '6': '3', '7': '1', '8': '2', '9': '4'
}
inverse_morse = {v: k for k, v in morse.items()}
special = [" ", ".", ",", ";", "[", "]", "}", "{", "*", "!", "@", "#", "%", "^", "&", "(", ")", "`", "~"]

# Building function for encoding to Morse code
def to_morse_code(message):
    morsecode = ''
    for data in message.upper():
        if data in morse:
            morsecode += morse[data]
        elif data in special:
            morsecode += data  # Preserve special characters as they are
        else:
            morsecode += '?'  # Placeholder for unsupported characters
    return morsecode

# Building function for decoding from Morse code
def to_normal(message):
    normal = ''
    i = 0
    while i < len(message):
        if message[i] in inverse_morse:
            normal += inverse_morse[message[i]]
            i += 1
        elif message[i] in special:
            normal += message[i]
            i += 1
        else:
            normal += '?'  # Placeholder for unsupported characters
            i += 1
    return normal

# MAIN SCREEN
def main():
    x=1
    while x==1 or x==2:
        print("What do you wish to do?")
        print("1. Encode your words to Morse")
        print("2. Decode Morse to normal text")
        try:
            x = int(input("Your answer: "))
            while x == 1 or x == 2:
                if x == 1:
                    message = input("Enter the text you want to encode: ")
                    morsed = to_morse_code(message)
                    print("Encoded to Morse:", morsed)
                    x = int(input("Do you want to continue? 1 for encode, 2 for decode, any other number to exit: "))
                elif x == 2:
                    message = input("Enter the Morse code you want to decode: ")
                    demorsed = to_normal(message)
                    print("Decoded to normal text:", demorsed)
                    x = int(input("Do you want to continue? 1 for encode, 2 for decode, any other number to exit: "))
        except ValueError:
            print("Invalid input. Exiting...")

if __name__ == "__main__":
    main()
