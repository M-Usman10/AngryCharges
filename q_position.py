import numpy as np

import matplotlib.pyplot as plt


def force(E, B, q, r, v):
    return q * (np.array(E) + np.cross(v, B))


def position_estimator(E, B, q, r, v, m, dt):
    F = force(E, B, q, r, v)
    vn = F * dt / m + v
    rn = vn * dt + r
    return np.array([rn, vn])


def test_positon_estimator():
    t=1000
    n = 100000
    pos = np.zeros([n, 2, 3])
    p = ([0, 0, 0], [0, 0.1, 0])

    for i in range(0, n):
        pos[i] = p
        p = position_estimator([0, 1, 0], [0, 0,0.01 ], 1, p[0], p[1], 1, t/n)
        # if i%1 == 0:
        #     plt.scatter(p[0][0],p[0][1])

    plt.figure()
    plt.plot(pos[:, 0, 0], pos[:, 0, 1])
    plt.title('delta t = ' + str(t/n))
    plt.show()

#test_positon_estimator()