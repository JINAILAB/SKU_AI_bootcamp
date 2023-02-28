import numpy as np

print('게임을 시작합니다.')
ran = np.random.choice(np.arange(1, 10), 3)

while True:
    strike = 0
    ball = 0
    answer = list(map(int, input('0에서 9사이의 3숫자를 뛰어서 입력해주세요.').split()))
    for a_idx, ans in enumerate(answer):
        if ans in ran:
            if a_idx in np.where(ran == ans):
                strike += 1
            else:
                ball += 1

    if strike == 3:
        print('정답입니다.')
        break

    else:
        if strike == 0 and ball == 0:
            print('OUT!!')
        else:
            print(f'{strike}S {ball}B')



