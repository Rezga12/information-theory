import sys
import os
from os import path
import numpy as np


def file_to_matrix(f, sz):
    matrix = []
    matrix = f.read().split('\n')[:sz]
    matrix = list(map(list, matrix))
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
        ans_n, ans_k = n, n - k
        ans_matrix = file_to_matrix(dat_f, k)

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
        res_matrix = file_to_matrix(res_f, res_k)

        matrix_n = len(res_matrix)
        if len(res_matrix) != k or len(res_matrix[0]) != n:
            print('False : First line written dimensions doesn\'t match real dimensions')
            print('Written Dimensions (n, k) = ({}, {})'.format(n, k))
            print('Real Dimensions             ({}, {})'.format(
                len(res_matrix), len(res_matrix[0])))
            exit()

    # 1). check for dimensions
    if (ans_n != res_n) or (ans_k != res_k):
        print("False : Your and Answer's Diemnsions doesn't match")
        print("Should be   : [{} {}]".format(ans_n, ans_k))
        print("Your Answer : [{} {}]".format(res_n, res_k))
        exit()

    # 2). check for linear independece
    # ToDo

    # 3). check for scalar product of .dat and generated files to be 0
    for i in range(len(ans_matrix)):
        for j in range(len(res_matrix)):
            G_vec = ans_matrix[i]
            P_vec = res_matrix[j]
            result = np.dot(G_vec, P_vec) % 2
            if result != 0:
                print("False: Scalar(Dot) product is not 0")
                print("Vector G[{}]: {}".format(i, G_vec))
                print("Vector P[{}]: {}".format(j, P_vec))
                print("Dot Product = {}".format(result))
                exit()

    print("True")