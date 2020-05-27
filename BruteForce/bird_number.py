# https://www.acmicpc.net/problem/1568

bird_number = int(input())

index = 1
cnt = 0

while bird_number > 0:
    if index > bird_number:
        index = 1
    bird_number = bird_number - index
    index += 1
    cnt += 1

print(cnt)