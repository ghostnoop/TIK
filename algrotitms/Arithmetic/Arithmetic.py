import os
import argparse
from ArithmeticEncoder import ArithmeticEncoder
from ArithmeticalDecoder import ArithmeticalDecoder
from FileWriter import FileWriter
from FileReader import FileReader


class Arithmetic(object):
    @classmethod
    def compress(cls, file_in, file_out):
        with open(file_in, 'rb') as f:
            content = f.read()

        ae = ArithmeticEncoder(content)
        content_fraction, length, symbols_dict = ae.encode()

        fw = FileWriter(file_out)
        fw.write(content_fraction, length, symbols_dict)

    @classmethod
    def decompress(cls, file_in, file_out):
        fr = FileReader(file_in)
        content_fraction, length, symbols_dict = fr.read()

        ad = ArithmeticalDecoder(content_fraction, length, symbols_dict)
        decoded_content = ad.decode()

        with open(file_out, 'wb') as f:
            f.write(decoded_content)


if __name__ == '__main__':
    action_dict = dict(compress=Arithmetic.compress, decompress=Arithmetic.decompress)
    parser = argparse.ArgumentParser(description='Compress/Decompress files using arithmetic coding algorithm.')
    parser.add_argument('action', choices=action_dict.keys())
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()

    action = args.action
    params = [args.input, args.output]
    action_dict[action](*params)
