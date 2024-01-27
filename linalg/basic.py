from typing import List


def vector_dot_product(v1: List[int], v2: List[int]) -> int:
    assert len(v1) == len(v2)
    ret = 0
    for i in range(len(v1)):
        ret += v1[i] * v2[i]

    return ret


def matrix_dot_product(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    ret_rows, ret_cols = len(m1), len(m2[0])

    ret = []
    for i in range(ret_rows):
        curr_row = []
        for j in range(ret_cols):
            n = 0
            for k in range(len(m2)):
                n += m1[i][k] * m2[k][j]
            curr_row.append(n)
        ret.append(curr_row)

    return ret


def matrix_by_vector(m: List[List[int]], v: List[int]) -> List[int]:
    # ret: Wx
    assert all(len(v) == len(m_row) for m_row in m)
    assert len(m) == 2

    rows, cols = len(m), len(m[0])
    ret = []
    for i in range(rows):
        curr = vector_dot_product(m[i], v)
        ret.append(curr)

    return ret


def vector_by_matrix(v: List[int], m: List[List[int]]) -> List[List[int]]:
    # ret: x.T W
    assert len(v) == len(m)

    rows, cols = len(m), len(m[0])
    ret = []
    for i in range(cols):
        curr_row = 0
        for j in range(rows):
            curr_row += v[j] * m[j][i]
        ret.append(curr_row)

    return [[n] for n in ret]


def matrix_sum(m1, m2):
    assert len(m1) == len(m2)
    assert all(len(r1) == len(r2) for r1, r2 in zip(m1, m2))

    rows, cols = len(m1), len(m1[0])

    ret = []
    for i in range(rows):
        curr_row = []
        for j in range(cols):
            n = m1[i][j] + m2[i][j]
            curr_row.append(n)
        ret.append(curr_row)

    return ret


def identity(n):
    ret = []
    for i in range(n):
        curr_row = []
        for j in range(n):
            if i == j:
                curr = 1
            else:
                curr = 0
            curr_row.append(curr)
        ret.append(curr_row)

    return ret


def matrix_power(m, p):
    rows, cols = len(m), len(m[0])

    if p == 0:
        return identity(rows)

    if p == 1:
        return m

    ret = m.copy()
    for _ in range(p):
        ret = matrix_dot_product(ret, m)

    return ret


print(vector_dot_product([1, 2, 3], [4, 5, 6]))
print(matrix_by_vector(
    [[1, 2, 3],
    [4, 5, 6]],
    [1, 2, 3]
))
print(vector_by_matrix(
    [1, 2],
    [[1, 2, 3],
    [4, 5, 6]],
))

print(matrix_sum(
    [[1, 2, 3],
     [2, 3, 4],
     [1, 1, 1]],
    [[4, 5, 6],
     [7, 8, 9],
     [4, 5, 7]]
))

print(matrix_power(
    [[1, 2, 3],
     [2, 3, 4],
     [1, 1, 1]],
    2
))

print(matrix_dot_product(
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
))

print(identity(5))
