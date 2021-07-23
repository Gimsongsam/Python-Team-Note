def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        t = []
        for x, y in zip(a, b):
            t.append(x + y)
        answer.append(t)
    return answer

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
