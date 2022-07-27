import json
f = open('keys.json')

keys = json.load(f)

def encode(msg):
    msg_words = msg.split()

    for word_index , word in enumerate(msg_words):
        word_letter = list(word)

        for letter_index , letter in enumerate(word_letter):
            word_letter[letter_index] = keys[letter]
        msg_words[word_index] = "".join(word_letter)
    return " ".join(msg_words)
def decode(msg):
    msg_words = msg.split()

    for word_index , word in enumerate(msg_words):
        word_letter = list(word)

        for letter_index , letter in enumerate(word_letter):
            word_letter[letter_index] = get_key_from_value(keys , letter)
        msg_words[word_index] = "".join(word_letter)
    return " ".join(msg_words)           

def get_key_from_value(dict , val):
    for key,value in dict.items():
        if value == val:
            return key                

while True:
    encode_or_decode = input("Do you want to encode or decode (E/D): ")

    match str.lower(encode_or_decode):
        case "e":
            print("Starting encoding....")

            #do encoding

            msg_to_encode = input("Message you want to encode : ")

            print(f'Encoded message : {encode(str.lower(msg_to_encode))}')

            break
        case "d":
            print("Starting decoding....")

            #do decoding
            msg_to_decode = input("Message you want to decode : ")

            print(f'Decoded message : {decode(str.lower(msg_to_decode))}')

            break
        case _:
            print("Please input either E or D")
