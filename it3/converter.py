import os


def get_size(filename):
    st = os.stat(filename)
    return st.st_size


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


class Converter:

    def __init__(self, filename, opt):
        self.file = open(filename, opt)
        self.byte = None
        self.reached_end = False
        self.file_size = get_size(filename)
        #print(self.file_size)

    def read_byte(self):
        final_byte = ''
        byte = self.file.read(1)

        if byte == b'':
            return None

        for i in range(8):
            final_byte += str(0 if int(byte[0]) & (1 << (7 - i)) == 0 else 1)

        return final_byte

    def read_string_byte(self):
        byte = self.file.read(8)
        if byte == b'':
            return None
        return bitstring_to_bytes(byte)

    def read_byte_epically(self):
        print(123)
        if self.reached_end:
            return None

        byte = self.file.read(8)
        if len(byte) < 8:
            self.reached_end = True
            byte += '1'
            for i in range(len(byte), 8):
                byte += '0'

        return bitstring_to_bytes(byte)

    def read_string_byte_epically(self):
        byte = self.file.read(1)

        final_byte = ''
        a = 8

        if byte == b'':
            return None

        if self.file_size - self.file.tell() == 0:

            for i in range(8):
                if int(byte[0]) & (1 << (7 - i)) != 0:
                    a = i

        for i in range(a):
            final_byte += str(0 if int(byte[0]) & (1 << (7 - i)) == 0 else 1)

        return final_byte
