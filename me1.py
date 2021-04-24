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
    n = int(input("input: "))
    print("result:", pinsetter_formula(n))
    print("result:", pinsetter_recursion(n))
    print("result:", pinsetter_loop(n))
