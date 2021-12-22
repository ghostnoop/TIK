import json
import math
import operator
from collections import Counter
from pprint import pprint

import numpy as np

from services import file_service, util_service

# Фано
class ShanonFanno(object):
    def __init__(self):
        self.sorted_s = []
        self.char_dict = dict()
        self.encoded_dict = dict()
        self.encoded_string = ''

    def code_tree(self, symbols):
        if len(symbols) == 2:
            self.encoded_dict[symbols[0]] += '0'
            self.encoded_dict[symbols[1]] += '1'
        elif len(symbols) > 2:
            breaking_index = self.break_the_node(symbols)
            for i in range(len(symbols)):
                left_part = i <= breaking_index
                if left_part:
                    self.encoded_dict[symbols[i]] += '0'
                else:
                    self.encoded_dict[symbols[i]] += '1'
            self.code_tree(symbols[:breaking_index + 1])
            self.code_tree(symbols[breaking_index + 1:])

    def make_count(self):
        self.char_dict = dict(Counter(self.sentence))
        char_ls = sorted(self.char_dict.items(), key=operator.itemgetter(1), reverse=True)
        sorted_s = []
        for i in char_ls:
            sorted_s.append(i[0])
        return self.char_dict, sorted_s

    def break_the_node(self, node):
        total = 0
        for i in range(len(node)):
            total += self.char_dict[node[i]]
        length = len(node)
        count = 0
        last_char_index = 0
        for i in range(length):
            count += self.char_dict[node[i]]
            if (count - (total / 2) < 0):
                last_char_index += 1
        return last_char_index

    def display_compressed(self):
        print("the encoded string:")
        for ch in self.sentence:
            print(self.encoded_dict[ch], end="")
        print(end='\n')
        print(str(self.encoded_dict))

    def encode(self, s):
        self.sentence = s
        self.total = len(s)
        self.char_dict, self.sorted_s = self.make_count()
        self.encoded_dict = {new_list: '' for new_list in self.sorted_s}
        self.code_tree(self.sorted_s)
        for ch in self.sentence:
            self.encoded_string += self.encoded_dict[ch]
        return self.encoded_string

    def decode(self, encoded_string, dictionary):
        holder = []
        codes = list(dictionary.values())
        symbols = list(dictionary.keys())
        inv_dictionary = dict(zip(codes, symbols))
        while (len(encoded_string) != 0):
            for code in codes:
                if encoded_string.startswith(code):
                    holder.append(inv_dictionary.get(code))
                    encoded_string = encoded_string[len(code):]
        print(''.join(holder))

        # return holder


if __name__ == '__main__':
    shf = ShanonFanno()


    def encode():
        print('==encode==')
        text = file_service.read_line('to_encode_tik.txt')
        s = list(text)
        shf.encode(s)
        shf.display_compressed()


    def decode():
        print('==decode==')
        code, tree = file_service.read_line('to_decode_tik.txt').strip().split('\n')
        shf.decode(code, util_service.from_str_to_dict(tree))


    encode()
    print()
    decode()
