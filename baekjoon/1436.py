#영화감독 숌

n = int(input())
cnt = 0 #몇번째 종말의 숫자인지
num = 666

while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1