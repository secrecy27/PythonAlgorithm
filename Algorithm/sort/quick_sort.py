# 퀵정렬 개념
# 1. 리스트 가운데서 하나의 원소를 고른다. 이를 피벗이라한다.
# 2. 피벗 앞에는 피벗보다 작은 원소들을 뒤에는 큰 원소들을 오게 한 후
#    피벗을 기준으로 리스트를 둘로 나눈다. 이렇게 나누는 것을 분할이라 하며 피벗은 더이상 움직이지 않는다.
# 3. 분할된 두개의 작은 리스트를 recursion으로 이 과정을 반복한다.
# # 리스트의 크기가 0이나 1이 될 때 까지 반복한다.


def quick_sort(a):
    # 퀵정렬 종료조건
    if len(a) <= 1:
        return a

    # 피벗 원소를 고른다.
    pivot = a[len(a) // 2]

    less = []
    equal = []
    more = []

    for i in a:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)

    return quick_sort(less) + equal + quick_sort(more)


a = [5, 6, 3, 4, 2, 1]

print(quick_sort(a))


def partition(a, start, end):
    pivot = a[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and a[left] <= pivot:
            left += 1
        while left <= right and pivot <= a[right]:
            right -= 1
        if right < left:
            done = True
        else:
            a[left], a[right] = a[right], a[left]

    a[start], a[right] = a[right], a[start]

    return right


def quick_sort2(a, start, end):
    if start < end:
        pivot = partition(a, start, end)
        quick_sort2(a, start, pivot - 1)
        quick_sort2(a, pivot + 1, end)
    return a


print(quick_sort2(a, 0, len(a) - 1))

def quick_sort3(a, left,right):
    if left<right:
        i=left
        j=right
        pivot=a[left]
        while i<j:
            while a[j]>pivot:
                j-=1
            while i<j and a[i]<=pivot :
                i+=1

            a[i],a[j]=a[j],a[i]

        a[left]=a[i]
        a[i]=pivot

        quick_sort3(a, left, i-1)
        quick_sort3(a, i+1, right)


d = [5, 6, 3, 4, 2, 1]
quick_sort3(d,0,len(d)-1)
print(d)