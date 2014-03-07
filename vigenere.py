import argparse

ALPHA_MIN = 33
ALPHA_MAX = 127
ALPHA_SHIFT = ALPHA_MAX - ALPHA_MIN

def encrypt(message, key, direction):
    expanded_key = expand_key(key, len(message))
    result = ""
    for message_letter, key_letter in zip(message, expanded_key):
        result += shift_letter(message_letter, key_letter, direction)
    return result


def expand_key(key, message_length):
    while len(key) < message_length:
        key = key + key
    return key

def shift_letter(message_letter, key_letter, shift_direction):

    if message_letter == " ":  # leaves spaces as-is
        return " "

    # because numbers
    letter_ordinal = ord(message_letter)
    key_ordinal = ord(key_letter) - ALPHA_MIN

    if shift_direction:
        shifted_ordinal = letter_ordinal + key_ordinal
    else:
        shifted_ordinal = letter_ordinal - key_ordinal

    # rotate the letters if they're out of range
    if shifted_ordinal <= ALPHA_MIN:
        shifted_ordinal = shifted_ordinal + ALPHA_SHIFT
    if shifted_ordinal >= ALPHA_MAX:
        shifted_ordinal = shifted_ordinal - ALPHA_SHIFT

    print "shifting %s (%s) with %s (%s) to %s (%s)" % (message_letter, letter_ordinal, key_letter, key_ordinal, chr(shifted_ordinal), shifted_ordinal)

    return chr(shifted_ordinal)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", required=True, help="What message are you trying to encrypt?")
    parser.add_argument("-k", "--key", required=True, help="What is the key for this message?")
    parser.add_argument("-d", "--direction", required=True, help="Encrypt or Decrypt?")
    args = parser.parse_args()
    
    if args.direction.lower() in ["e", "encrypt"]:
        result = encrypt(args.message, args.key, True)
    elif args.direction.lower() in ["d", "decrypt"]:
        result = encrypt(args.message, args.key, False)

    print result