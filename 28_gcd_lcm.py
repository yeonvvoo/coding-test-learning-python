'''
#BOJ 1934 최소공배수

[문제설명]

[문제풀이]
    * 최대공약수 gcd Greatest Common Divisor
        : 유클리드 호제법 Euclidean Algorithm
            O(logN)
            a와 b의 최대공약수
            = b와 a%b의 최대공약수
            = ...
            = a%b가 0인 순간 b의 값이 최대공약수

    * 최소공배수 lcm Least Common Multiple
        : a와 b의 최소공배수
         = a*b / (a와b의 gcd)

    def gcd(a, b):
        if a<b:
            temp = a
            a = b
            b = temp

        if a%b==0:
            return b
        else:
            return gcd(b, a%b)

    def lcm(a, b):
        return a*b / gcd(a, b)
[어려웠던 점 & 다시 공부할 부분]

'''


def gcd(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return a*b / gcd(a, b)

T = int(input())

for t in range(T):
    a, b = map(int, input().split())

    print(int(lcm(a,b)))