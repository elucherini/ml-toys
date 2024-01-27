def no_solution():
    """
    HackerRank: There are more than one integer values of  for which the following system of
    equations in x, y, z has no solutions:

    ax + y + 2 z = 0
    x + 2 y + z = b
    2 x + y + az = 0

    What is the smallest integer value of  for which the above system has no solutions?
    """
    # Equation:
    # |a 1 2| |x|   |0|
    # |1 2 1| |y| = |b|
    # |2 1 a| |z|   |0|
    #
    # determinant:
    # 2a^2 - 2a - 4
    for i in range(1, 10000000):
        det = 2 * i**2 - 2 * i - 4
        if det == 0:
            return i

    assert False


def determinant(m):
    # Only 2x2 for now
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def eigen_2x2(m):
    assert len(m) == 2 and len(m[0]) == 2
    # (M - lambda * I) = 0
    #
    # | (m1 - lambda1) m2 |
    # | m3 (m4 - lambda2) | = 0
    #
    # det = lambda^2 - (m1 + m4) * lambda + a1*a4 - a2*a3 = 0
    # try for values of lambda until det == 0, or calculate them exactly
    eigenvalues = []
    for l in range(-10, 11):
        det = (m[0][0] - l) * (m[1][1] - l) - m[0][1] * m[1][0]
        if det == 0:
            eigenvalues.append(l)

    return eigenvalues


print(no_solution())
print(eigen_2x2(
    [[0, 1],
     [-2, -3]]
))
