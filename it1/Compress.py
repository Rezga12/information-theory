import sys
import converter


def read_byte_epically(byte):
    #print(byte)
    if len(byte) < 8:
        byte += '1'
        for i in range(len(byte), 8):
            byte += '0'

    return converter.bitstring_to_bytes(byte)


def main():
    file = open(sys.argv[1])
    characters = [' ', 'ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ',
                       'რ', 'ს', 'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']

    mapp = dict()

    for char in characters:
        mapp[char] = file.readline().strip('\n')

    #print(mapp)

    text = open(sys.argv[2])
    code = ''
    char = text.read(1)
    while char:
        code += mapp[char]
        char = text.read(1)

    output = open(sys.argv[3], 'wb')

    while True:
        if len(code) < 8:
            output.write(read_byte_epically(code))
            break

        byte = code[:8]
        code = code[8:]
        output.write(read_byte_epically(byte))






if __name__ == '__main__':
    main()
