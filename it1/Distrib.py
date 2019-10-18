import sys


def main():

    filename = sys.argv[1]
    file = open("Public Tests/A/001.dat")

    total_count = 0
    dic = dict()
    dic_two = dict()
    char = file.read(1)
    prev_char = ' '
    while char:

        if char in dic.keys():
            dic[char] += 1
        else:
            dic[char] = 1

        if prev_char + char in dic_two:
            #print(prev_char + char)
            dic_two[prev_char + char] += 1
        else:
            dic_two[prev_char + char] = 1

        total_count += 1
        prev_char = char
        char = file.read(1)

    keys = dic_two.keys()
    keys = sorted(keys)
    #for k in keys:
    #   print(round(float(dic_two[k]) / (total_count - 1), 7))


if __name__ == "__main__":
    main()