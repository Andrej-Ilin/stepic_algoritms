"""Даны целые числа 1 ≤ n ≤ 10^18 и  2 ≤ m ≤ 10^5, необходимо найти остаток от деления n-го числа
Фибоначчи на m.

Sample Input:
10 2
Sample Output:
1
"""

def fib_mod(n, m):

    f = [0, 1, 1]
    i = 2
    while (f[i] != 1 or f[i - 1] != 0):
        f.append((f[i - 1] + f[i]) % m)
        i += 1
    T = i - 1
    return(f[n % T])

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()