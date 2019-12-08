import sys


def has_one(mat, ind, j):

    for i in range(ind, len(mat)):
        if mat[i][j] == '1':
            return True

    return False


def add(mat, ind, line):
    for i in range(len(line)):
        if mat[ind][i] == line[i]:
            mat[ind][i] = '0'
        else:
            mat[ind][i] = '1'




def make_it_good(mat, ind, j):
    _line = ''
    for i in range(ind, len(mat)):
        if mat[i][j] == '1':
            _line = mat[i]
            break

    if mat[ind][j] == '0':
        add(mat, ind, _line)

    _line = mat[ind]


    for i in range(ind+1, len(mat)):
        if mat[i][j] == '1':
            add(mat, i, _line)


def swap(mat, a, b):

    for i in range(len(mat)):
        k = mat[i][a]
        mat[i][a] = mat[i][b]
        mat[i][b] = k


def main():
    in_file = open(sys.argv[1])
    out_file = open(sys.argv[2], 'w+')

    nums = in_file.readline().split(' ')
    n = int(nums[0])
    k = int(nums[1])

    mat = []
    for i in range(k):
        mat.append(list(in_file.readline())[0:n])

    dic = dict()
    dif = dict()
    for i in range(n):
        dif[i] = i


    for i in range(k):
        for j in range(n):
            if has_one(mat, i, j):
                make_it_good(mat, i, j)
                dic[j] = i
                break


    # for i in mat:
    #     print(i)




    for i in dic.keys():
        a = dic[i]
        swap(mat, i, a)
        p = dif[a]
        g = dif[i]
        dif[i] = p
        dif[a] = g

    # print(dif.values())
    #
    # for i in mat:
    #     print(i)

    for ii in range(0, k):
        i = k - ii - 1
        for j in range(0,i):
            if mat[j][i] == '1':
                add(mat, j, mat[i])

    out_file.write(str(n) + " " + str(k) + "\n")
    tt = map(lambda aa: "".join(aa)+"\n", mat)
    out_file.writelines(tt)
    out_file.write(" ".join(map(lambda gg: str(gg+1), list(dif.values()))))

if __name__ == '__main__':
    main()