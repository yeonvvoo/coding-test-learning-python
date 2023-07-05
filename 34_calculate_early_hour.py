'''
#BOJ 2884 알람 시계

[문제설명]
    시각이 주어졌을때
    그 시각보다 45분 이른 시각을 출력해라

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    m==45일때를 빠트려서 첫 시도때 틀렸다.
    m>45아니고 m>=45여야 했다.
'''

h, m = map(int, input().split())

if m>=45:
    m = m-45
else:
    h = (h-1) % 24
    m = (m+15) % 60

print(h, m)