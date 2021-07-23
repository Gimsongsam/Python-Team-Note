# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array) # [1, 3, 6, 9, 11, 13, 15, 17, 19]


# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]

print(array)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# N ✕ M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]

print(array) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

