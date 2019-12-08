import sys


def has_one(mat, ind, j):

    for line in mat:
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


def setVerticalLine(parity, oldpar, i, oi):
    for j in range(len(parity)):
        parity[j][i] = oldpar[j][oi]


def get_combs(n, soFar, arr, l):
    if n == 0:
        arr.append(soFar)
        return

    for i in range(l, len(soFar)):
        tt = soFar[i]
        soFar[i] = '1'
        get_combs(n-1, soFar[:], arr,i)
        soFar[i] = tt


def mult(parity, s):
    res = []

    for i in range(len(parity)):
        a = 0
        for j in range(len(s)):
            a += int(parity[i][j]) * int(s[j])
        res.append(str(a % 2))

    return res




def main():
    in_file = open(sys.argv[1])
    out_file = open(sys.argv[3], 'w+')
    num = int(open(sys.argv[2]).readline())

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


    for i in dic.keys():
        a = dic[i]
        swap(mat, i, a)
        p = dif[a]
        g = dif[i]
        dif[i] = p
        dif[a] = g

    diff = [0] * n
    for i in sorted(dif.keys()):
        diff[dif[i]] = i


    for ii in range(0, k):
        i = k - ii - 1
        for j in range(0, i):
            if mat[j][i] == '1':
                add(mat, j, mat[i])



    parity = []
    newPar = []
    for ii in range(n-k):
        i = k + ii
        a = []
        na = []
        for j in range(k):
            a.append(mat[j][i])
            na.append('9')
        a.extend((n-k) * ['0'])
        na.extend((n-k)*'9')
        a[k+ii] = '1'
        parity.append(a)
        newPar.append(na)




    for i in range(n):
         setVerticalLine(newPar,parity,i,diff[i])

    out_file.write(str(n) + " " + str(n-k) + "\n")
    tt = map(lambda aa: "".join(aa)+"\n", newPar)
    out_file.writelines(tt)

    arr = []
    h = []
    for i in range(n):
        h.append('0')
    arr.append(h)


    get_combs(num,h[:],arr,0)
    # print(arr)
    syndroms = list(map(lambda x: mult(newPar, x), arr))

    for i in range(len(arr)):
        out_file.write("".join(arr[i]) + ' ' + "".join(syndroms[i]) + "\n")


if __name__ == '__main__':
    main()