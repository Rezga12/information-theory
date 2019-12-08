import sys
import os
from os import path
import numpy as np


def file_to_matrix(f, with_permutations=False):
    info = f.read().split('\n')
    if with_permutations:
        matrix = list(map(list, info[:-1]))
        for i in range(len(matrix)):
            s = matrix[i]
            matrix[i] = list(map(int, s))
        perms = info[-1].split()
        perms = list(map(int, perms))
        return matrix, perms
    else:
        matrix = list(map(list, info))
        for i in range(len(matrix)):
            s = matrix[i]
            matrix[i] = list(map(int, s))
        return matrix


if __name__ == "__main__":
    ans_file = sys.argv[1]
    dat_file = sys.argv[2]
    res_file = sys.argv[3]

    # If program didn't create file exit
    if not path.exists(res_file):
        print('False : File Doesn\'t exist (Your program didn\'t create file)')
        exit()

    # check if generated file is empty
    if os.stat(res_file).st_size == 0:
        print('False : File is empty')
        exit()

    # read .dat file
    ans_n, ans_k = 0, 0
    with open(dat_file, 'r') as dat_f:
        n, k = map(int, dat_f.readline().split())
        ans_n, ans_k = n, k
        ans_matrix = file_to_matrix(dat_f)

    # read generated file
    res_n, res_k = 0, 0
    with open(res_file, 'r') as res_f:
        ll = res_f.readline()
        lst = list(map(int, ll.split()))
        if len(lst) != 2:
            print("False : First line should contain 2 Integers (n,k)")
            print("Your File contains {} Integers".format(len(lst)))
            exit()
        n, k = lst
        res_n, res_k = n, k
        res_matrix, permutations = file_to_matrix(res_f, True)

    # 1). check for dimensions
    if ans_n != res_n or ans_k != res_k:
        print("False : Diemnsions doesn't match")
        print("Should be   : [{} {}]".format(ans_n, ans_k))
        print("Your Answer : [{} {}]".format(res_n, res_k))
        exit()

    # 2). check for I matrix
    for i in range(ans_k):
        for j in range(ans_k):
            val = res_matrix[i][j]
            if (i != j and val != 0) or ((i == j and val == 0)):
                print("False : Matrix not in Standard form")
                print("G[{}][{}]={}".format(i, j, val))
                exit()

    # 3). check for corectness
    # ToDo

    print('True')
