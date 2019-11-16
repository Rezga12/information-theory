import sys
import os

def get_elias(size):

    bina = '{0:b}'.format(size)

    elias = '0' * (len(bina) - 1) + bina
    return elias


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


def read_string_byte(byte):

    if byte == b'':
        return None
    return bitstring_to_bytes(byte)


def read_byte(byte):
    final_byte = ''

    if byte == b'':
        return None

    for i in range(8):
        final_byte += str(0 if int(byte[0]) & (1 << (7 - i)) == 0 else 1)

    return final_byte


class Bitter:
    def __init__(self,filename):
        self.file = open(filename, 'rb')
        self.current_byte = self.read_byte()

    def read_byte(self):
        final_byte = ''
        byte = self.file.read(1)

        if byte == b'':
            return None

        for i in range(8):
            final_byte += str(0 if int(byte[0]) & (1 << (7 - i)) == 0 else 1)

        return final_byte

    def get_next_bit(self):

        if self.current_byte:
            rv = self.current_byte[0]
            self.current_byte = self.current_byte[1:]

            if len(self.current_byte) == 0:
                self.current_byte = self.read_byte()
        else:
            rv = ''

        return rv

    def has_next_bit(self):
        if not self.current_byte:
            return False
        return True



def main():
    in_file = sys.argv[1]
    size = os.stat(in_file).st_size
    code = get_elias(size)

    dic = {'0': '0',
           '1': '1'}

    bitter = Bitter(in_file)

    bits = ''
    finished = False

    while not finished:
        if bitter.has_next_bit():
            bits += bitter.get_next_bit()
        else:
            bits += '0'

        if bits in dic:
            if not bitter.has_next_bit():
                finished = True

            k = bits
            # print(dic)
            v = dic[k]
            code += v
            bits = ''
            dic.pop(k)
            dic[k + '0'] = v
            dic[k + '1'] = '{0:b}'.format(len(dic))
            if len(dic[k + '1']) > len(v):
                # print(1)
                for key in dic.keys():
                    if key != k + '1':
                        a = dic[key]
                        dic[key] = '0' + a

    print(len(code))

    padding = 8 - len(code) % 8

    code += '1' + (padding-1) * '0'

    out = open(sys.argv[2], 'wb')
    out.write(bitstring_to_bytes(code))

    print(len(code))

    # out_file = sys.argv[2]


if __name__ == '__main__':
    main()
