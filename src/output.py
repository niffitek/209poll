from math import sqrt


def calc_variance(pSize, sSize, p):
    p /= 100
    denominator = (p * (1 - p)) * (pSize - sSize)
    numerator = sSize * (pSize - 1)
    return denominator / numerator


def func(x):
    return x * 100.0 / 2.0


def calc_confidence(variance):
    return func(2 * 1.96 * sqrt(variance)), func(2 * 2.58 * sqrt(variance))


def output(pSize, sSize, p):
    print("Population size:\t\t\t" + str(pSize))
    print("Sample size:\t\t\t\t" + str(sSize))
    print("Voting intentions:\t\t\t%.2f%%" % p)
    variance = calc_variance(pSize, sSize, p)
    print("Variance:\t\t\t\t\t%.6f" % variance)
    confidence1, confidence2 = calc_confidence(variance)
    print("95%% confidence interval:\t[%.2f%%; %.2f%%]" % (max(0, p - confidence1), min(100, p + confidence1)))
    print("99%% confidence interval:\t[%.2f%%; %.2f%%]" % (max(0, p - confidence2), min(100, p + confidence2)))

