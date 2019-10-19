import sys
import math


def generate_codes(choice, so_far, lengths, mapp):
    if len(lengths) == 0:
        return

    so_far += str(choice)
    if len(so_far) in lengths:
        index = lengths.index(len(so_far))
        if lengths[index] not in mapp:
            mapp[lengths[index]] = [so_far]
        else:
            mapp[lengths[index]].append(so_far)
        lengths.pop(index)
    else:
        generate_codes(1, so_far, lengths, mapp)
        generate_codes(0, so_far, lengths, mapp)



def main():

    file = open(sys.argv[1])
    n = int(file.readline())

    lengths = list(map(int, file.readline().split(' ')))

    total_sum = sum(map(lambda x: math.pow(2, -x), lengths))

    if total_sum <= 1:
        mapp = dict()
        #print(sorted(lengths))
        a = lengths[:]
        generate_codes(1, '', a, mapp)
        generate_codes(0, '', a, mapp)

        output = open(sys.argv[2], 'w+')

        for elem in lengths:
            output.write(mapp[elem][0] + "\n")
            mapp[elem].pop(0)


if __name__ == "__main__":
    main()
