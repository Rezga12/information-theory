import sys
from converter import Converter
import timeit

def mult(parity, s):
    res = ""

    for i in range(len(parity[0])):
        a = '0'
        for j in range(len(s)):
            res1 = '0'
            if parity[j][i] == '1' and s[j] == '1':
                res1 = '1'


            if a == res1:
                a = '0'
            else:
                a = '1'

        res += a
    #print(res)
    return res


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')





def main():
    code = open(sys.argv[1])
    # in_file = open(sys.argv[2])


    nums = code.readline().split(' ')
    n = int(nums[0])
    k = int(nums[1])

    con = Converter(sys.argv[2], 'rb')

    bytess = ""

    byte = con.read_byte()
    while byte is not None:
        bytess += byte
        byte = con.read_byte()

    # print(bytess)

    # bytess = list(bytess)




    mat = []
    for i in range(k):
        mat.append(list(code.readline())[0:n])

    codewords = ""

    while len(bytess) > 0:
        codeword = bytess[:k]
        bytess = bytess[k:]

        codewords += mult(mat, codeword)

    gg = ''
    if len(codewords) % 8 == 0:
        codewords += "10000000"
    else:
        gg = codewords[-(len(codewords) % 8):]
        codewords = codewords[:-(len(codewords) % 8)]

        gg += '1'
        while len(gg) != 8:

            gg += '0'
        codewords += gg
        # print(gg)

    #print(codewords)

    bits = bitstring_to_bytes(codewords)

    out_file = open(sys.argv[3], 'wb')
    out_file.write(bits)


if __name__ == '__main__':
    #start = timeit.default_timer()

    main()

    #stop = timeit.default_timer()

    #print('Time: ', stop - start)
