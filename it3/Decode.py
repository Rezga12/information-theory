import sys
from converter import Converter


def read_byte(byte):

    if byte == b'':
        return None

    return bin(int(byte[0])).lstrip('0b').zfill(8)

def mult(parity, s):
    res = []

    for i in range(len(parity)):
        a = 0
        for j in range(len(s)):
            a += int(parity[i][j]) * int(s[j])
        res.append(str(a % 2))

    return res


def fix(syndrome,codeword):
    for i in range(len(syndrome)):
        if syndrome[i] == '1':
            if codeword[i] == '1':
                codeword[i] = '0'
            else:
                codeword[i] = '1'
    return codeword

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def main():
    info = open(sys.argv[1])
    out_file = open(sys.argv[3], 'wb')

    nums = info.readline().split(' ')
    n = int(nums[0])
    k = int(nums[1])

    parity = []
    for i in range(k):
        parity.append(list(info.readline())[0:n])

    dline = info.readline()
    syndrome_dic = dict()
    while dline:
        arr = dline.split(' ')
        syndrome_dic[arr[1].strip('\n')] = arr[0]
        dline = info.readline()


    in_file = open(sys.argv[2],'rb')

    bytess = ""

    byte = in_file.read(1)
    while byte != b'':
        byte = read_byte(byte)
        bytess += byte
        byte = in_file.read(1)

    pad = ""
    while bytess[-1] == '0':
        pad += '0'
        bytess = bytess[:-1]

    bytess = bytess[:-1]
    pad = '1' + pad

    ans = ""
    while len(bytess) > 0:
        codeword = bytess[:n]
        bytess = bytess[n:]
        syndrome = syndrome_dic["".join(mult(parity,codeword))]

        fixed_word = fix(syndrome,list(codeword))

        ans += "".join(fixed_word)

    out_file.write(bitstring_to_bytes(ans+pad))






if __name__ == '__main__':
    main()