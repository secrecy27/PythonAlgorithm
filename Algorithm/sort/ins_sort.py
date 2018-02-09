# 삽입정렬

def ins_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1  # j가 i에 왼쪽 위치로 저장

        while j >= 0 and a[j] > key:
            # key는 i위치의 값이므로 a[j]가 클 경우 위치변경
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


d = [2, 4, 5, 1, 3]

ins_sort(d)

print(d)
