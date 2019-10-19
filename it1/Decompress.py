import sys
from converter import *


def main():
    file = open(sys.argv[1])
    characters = [' ', 'ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ',
                  'რ', 'ს', 'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']

    mapp = dict()

    char = file.readline().strip('\n')
    i = 0
    while char:
        mapp[char] = characters[i]
        char = file.readline().strip('\n')
        i += 1

    conv = Converter(sys.argv[2], 'rb')

    byte = conv.read_string_byte_epically()
    code = ''
    while byte is not None:
        code += byte
        byte = conv.read_string_byte_epically()

    output = open(sys.argv[3],'w+')
    so_far = ''
    for ch in code:
        so_far += ch

        if so_far in mapp:
            output.write(mapp[so_far])
            so_far = ''



if __name__ == '__main__':
    main()