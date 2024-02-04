import sys


def binary_search(n, A, k, i):
    l = 0
    r = n - 1
    while l <= r:
        m = l + (r - l) // 2
        if A[m] == i:
            return m + 1
        elif A[m] > i:
            r = m - 1
        else:
            l = m + 1
    return -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *A = next(reader)
    k, *b = next(reader)
    CollectIndex = [binary_search(n, A, k, i) for i in b]
    print(*CollectIndex)


if __name__ == '__main__':
    main()
