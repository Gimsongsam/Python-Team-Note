n, m = map(int, input().split()) # 행의 개수 n, 열의 개수 m

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

''''''''''''''''''''''''''''''

# 딕셔너리 최대 value에 대한 key 찾기
di = {'a': 0, 'b': 1, 'c': 2, 'd': 3} # 직접 생성
di = dict(zip('abcd',range(4))) # zip 함수를 사용해 dict 생성: zip(key list, value list)

result = [k for k,v in di.items() if max(di.values()) == v]
