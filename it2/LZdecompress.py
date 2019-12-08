import sys
import os


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


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def main():
    in_file = sys.argv[1]

    bitter = Bitter(in_file)
    elias_size = 0
    elias_bin = '1'


    bit = bitter.get_next_bit()
    while bit != '1':
        elias_size += 1
        bit = bitter.get_next_bit()

    for i in range(elias_size):
        elias_bin += bitter.get_next_bit()

    size = int(elias_bin, 2)


    dic = {'0': '0',
           '1': '1'}

    finished = False
    bits = ''
    code = ''

    while not finished:
        if bitter.has_next_bit():
            bits += bitter.get_next_bit()
        #print(bits)
        if bits in dic:

            code += dic[bits]
            v = dic[bits]
            dic.pop(bits)
            dic[bits] = v + '0'
            n = '{0:b}'.format(len(dic))
            dic[n] = v + '1'

            if len(n) > len(bits):

                arr = dic.keys()
                arr = list(arr)

                for key in arr:
                    if key != n:
                        a = dic[key]
                        dic.pop(key)
                        dic['0' + key] = a
            # print(dic)
            bits = ''
        if len(code) >= 8 * size:
            break

    code = code[:(8 * size)]
    # print(dic)
    out = open(sys.argv[2], 'wb')
    out.write(bitstring_to_bytes(code))


if __name__ == '__main__':
    main()
