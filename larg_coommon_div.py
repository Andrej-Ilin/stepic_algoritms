"""По данным двум числам 1 ≤ a, b ≤ 2 ⋅ 10 найдите их наибольший общий делитель
Sample Input 1:

18 35
Sample Output 1:
1
Sample Input 2:
14159572 63967072
Sample Output 2:
4
"""

def gcd(a, b):
    return gcd(b, a % b) if b else a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()