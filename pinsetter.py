import pandas as pd
import timeit

# using sum of series concept, i.e., the n-th partial sum of a series is the sum of the first n terms.
# the formula used below is the sum of values of k, beginning at n_1 and ending with n_n, where k = (n*(n+1))/2.
def pinsetter_formula(n):
    return (n*(n+1))/2


def pinsetter_recursion(n):
    if (n > 0):
        result = n + pinsetter_recursion(n-1)
    else:
        result = 0
    return result


def pinsetter_loop(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


if __name__ == "__main__":
    d = {
        'Algorithm': ['Formula', 'Recursion', 'One Loop'],
        'Result': ['-', '-', '-'],
        'Speed': ['-', '-', '-']
    }

    df = pd.DataFrame(data=d)

    n = int(input("input: "))

    start_formula = timeit.default_timer()
    res_formula = pinsetter_formula(n)
    stop_formula = timeit.default_timer()

    start_loop = timeit.default_timer()
    res_loop = pinsetter_loop(n)
    stop_loop = timeit.default_timer()

    start_recursion = timeit.default_timer()
    res_rec = pinsetter_recursion(n)
    stop_recursion = timeit.default_timer()

    df.loc[0].Result = int(res_formula)
    df.loc[1].Result = res_rec
    df.loc[2].Result = res_loop

    df.loc[0].Speed = "{:e}".format(stop_formula-start_formula)
    df.loc[1].Speed = "{:e}".format(stop_recursion-start_recursion)
    df.loc[2].Speed = "{:e}".format(stop_loop-start_loop)

    print(df)
