# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

# 1, 2, 1+2, 2+(1+2), (1+2)+(2+1+2)

first = 1
second = 2

list = []

list.append(first)
list.append(second)


while first + second <= 4000000:
    list.append(first + second)
    temp = second
    second = first + second
    first = temp

print(list)

list_idx = 0
while list_idx < len(list):
    if list[list_idx] % 2 != 0:
        del list[list_idx]
        continue
    list_idx += 1

print(list)

list_idx = 0
sum = 0
while list_idx < len(list):
    sum += list[list_idx]
    list_idx += 1

print(sum)