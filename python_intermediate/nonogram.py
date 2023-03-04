"""
문제 3 : 네모네모 로직(nonogram) 숫자 채우기
아래 리스트에는 그림이 그려져있다.
' '(공백)과 0을 읽어서 각 열과 행에 해당하는 그림의 묶음을 구한다.
step 1, 2, 3중 하고싶은 걸 한다
상단과 하단의 숫자를 list로 출력한다 (step1 : 여기까지 난이도 중)
숫자를 예쁘게 배치해서 출력한다 (step 2: 난이도 +a)
그림과 같은 모양으로 출력한다 (step 3: 난이도 몹시 귀찮음)
"""
from typing import List

from collections import deque
import numpy as np

arr = [[' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', '0', '0'],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0'],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0'],
       [' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', ' '],
       ['0', '0', ' ', ' ', '0', '0', '0', '0', ' ', ' '],
       ['0', '0', ' ', '0', '0', '0', '0', '0', '0', ' '],
       [' ', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
       [' ', ' ', ' ', ' ', '0', ' ', ' ', '0', ' ', ' '],
       [' ', ' ', ' ', '0', '0', ' ', '0', '0', ' ', ' '], ]

maps = np.array(arr)

left = []
upper = []
print_upper = []
print_left = []

for row in maps:
    a = ''.join(row)
    a = a.split()
    upper.append(deque([len(i) for i in a]))
    print_upper.append([len(i) for i in a])

maps_transpose=maps.transpose()

for row in maps_transpose:
    a = ''.join(row)

    a = a.split()
    left.append(deque([len(i) for i in a]))
    print_left.append([len(i) for i in a])

print('문제1')
print(print_left)
print(print_upper)

upper_len = max([len(i) for i in left])
lower_len = max([len(i) for i in upper])

for idx, j in enumerate([upper_len - len(i) for i in left]):
    left[idx].extendleft([' ']*j)

for idx, j in enumerate([lower_len - len(i) for i in upper]):
    upper[idx].extendleft([' ']*j)

left = np.array(left).transpose()
upper = np.array(upper).transpose()

print('문제2')
for i in left:
    print(' '.join(i))
print('')
for i in upper:
    print(' '.join(i))

left = left.transpose()

lower = np.concatenate([left, arr], 1)
up = np.concatenate([np.full((upper.shape[0], left.shape[1]), ' '), upper], 1)
maps = np.concatenate([up, lower], 0)

print('문제3')
for i in maps:
    print(' '.join(i))


