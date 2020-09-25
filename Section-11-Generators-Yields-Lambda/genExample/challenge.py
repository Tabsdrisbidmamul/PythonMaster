def gen():
    start = 1
    while True:
        yield start
        start += 2


def pi_series():
    odds = gen()
    approx = 0
    while True:
        approx += (4 / next(odds))
        yield approx
        approx -= (4 / next(odds))
        yield approx


approx_pi = pi_series()

for x in range(100):
    print("approx {}".format(next(approx_pi)))
