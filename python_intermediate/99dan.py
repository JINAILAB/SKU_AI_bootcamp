import numpy as np

print('게임을 시작합니다. 1-20까지의 숫자를 입력하세요.')
ran = np.random.randint(1, 20)

while True:
    answer = int(input('숫자를 입력하세요.'))
    if answer > ran:
        print('UP!')

    elif answer < ran:
        print('Down!')

    else:
        print(f'정답입니다. 숫자는 {ran}이었습니다!!!')
        print('게임종료')
        break


