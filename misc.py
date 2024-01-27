from typing import List


def dot_product(v1: List[int], v2: List[int]) -> int:
    assert len(v1) == len(v2)
    ret = 0
    for i in range(len(v1)):
        ret += v1[i] * v2[i]

    return ret


def matrix_by_vector(m: List[List[int]], v: List[int]) -> List[int]:
    # ret: Wx
    assert all(len(v) == len(m_row) for m_row in m)
    assert len(m) == 2

    rows, cols = len(m), len(m[0])
    ret = []
    for i in range(rows):
        curr = dot_product(m[i], v)
        ret.append(curr)

    return ret


def vector_by_matrix(v: List[int], m: List[List[int]]) -> List[List[int]]:
    # ret: xTW
    assert len(v) == len(m)

    rows, cols = len(m), len(m[0])
    ret = []
    for i in range(cols):
        curr_row = 0
        for j in range(rows):
            curr_row += v[j] * m[j][i]
        ret.append(curr_row)

    return [[n] for n in ret]


print(dot_product([1, 2, 3], [4, 5, 6]))
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
