import argparse

def shift_message(message, shift):
    # shift each letter individually
    encrypted = ""
    for unshifted_letter in message:
        encrypted += shift_letter(unshifted_letter, shift)
    return encrypted

def shift_letter(letter, shift):

    if letter == " ":  # leaves spaces as-is
        return " "

    # because numbers
    ordinal = ord(letter)
    shifted_ordinal = ordinal + shift

    # rotate the letters if they're out of range
    if shifted_ordinal <= 97:
        shifted_ordinal = shifted_ordinal + 26
    if shifted_ordinal >= 123:
        shifted_ordinal = shifted_ordinal - 26
    return chr(shifted_ordinal)


if __name__ == '__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", required=True, help="What message are you trying to encrypt?")
    parser.add_argument("-s", "--shift", type=int, required=True, help="What is the shift key for this message?")
    parser.add_argument("-d", "--direction", required=True, help="Encrypt or Decrypt?")
    args = parser.parse_args()
    
    if args.direction.lower() in ["e", "encrypt"]:
        shift = args.shift
    elif args.direction.lower() in ["d", "decrypt"]:
        shift = 0-args.shift

    print shift_message(args.message, shift)