# 회문

# Collections : tuple, dict에 대한 확장 데이터 구조 제공
from collections import deque

qu = deque()
qu.append(1)
qu.append(2)

# qu.popleft() : 첫번째 항목을 삭제하고 반환
print(qu.popleft())  # 1
print(qu.popleft())  # 2


def palindrome(s):
    qu = []
    st = []

    for i in s:
        # i가 영문이면
        if i.isalpha():
            qu.append(i.lower())
            st.append(i.lower())

    while qu:
        # qu 리스트와 st 리스트 비교
        if qu.pop(0) != st.pop():
            return False
    return True


# 큐 사용 x
def palindrome2(s):
    i = 0
    j = len(s) - 1

    while i < j:
        # 영문인지만 판단
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


print(palindrome("Wow"))
print(palindrome2("Wow"))