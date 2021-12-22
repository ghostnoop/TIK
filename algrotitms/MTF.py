from typing import List, Tuple, Union


class MTF(object):

    # Instead of always transmitting an "original" dictionary, it is simpler to just agree on an initial set.
    # Here we use the 256 possible values of a byte:
    def __init__(self):
        self.common_dictionary = list(range(256))

    def encode(self, plain_text: str) -> List[int]:
        # Change to bytes for 256.
        plain_text = plain_text.encode('utf-8')

        # Changing the common dictionary is a bad idea. Make a copy.
        dictionary = self.common_dictionary.copy()

        # Transformation
        compressed_text = list()  # Regular array
        rank = 0

        # Read in each character
        for c in plain_text:
            rank = dictionary.index(c)  # Find the rank of the character in the dictionary [O(k)]
            compressed_text.append(rank)  # Update the encoded text

            # Update the dictionary [O(k)]
            dictionary.pop(rank)
            dictionary.insert(0, c)

        print(compressed_text)
        return compressed_text

    def decode(self, compressed_data: List[int]) -> str:
        compressed_text = compressed_data
        dictionary = self.common_dictionary.copy()
        plain_text = []

        # Read in each rank in the encoded text
        for rank in compressed_text:
            # Read the character of that rank from the dictionary
            plain_text.append(dictionary[rank])

            # Update the dictionary
            e = dictionary.pop(rank)
            dictionary.insert(0, e)

        text = bytes(plain_text).decode('utf-8')
        print(text)
        return text


if __name__ == '__main__':
    dt = MTF().encode('ewrwqer')
    MTF().decode(dt)
