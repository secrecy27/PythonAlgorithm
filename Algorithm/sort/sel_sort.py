# 선택정렬
# 1. 주어진 리스트 중에 최솟값을 찾는다.
# 2. 그 값을 맨 앞에 위치한 값과 교체한다.
# 3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.

def sel_sort(a):
    n = len(a)

    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            # 내림차순 정렬시
            if a[j] > a[min_idx]:
            # 오름차순 정렬시
            # if a[j]<a[min_idx]:
                a[j], a[min_idx] = a[min_idx], a[j]


d=[2,4,5,1,3]

sel_sort(d)

print(d)