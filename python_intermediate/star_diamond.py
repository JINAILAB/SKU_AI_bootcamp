"""
문제 1: 빛나는 다이아몬드 그리기 (하)
한 변이 n인 다이아몬드를 그린다. n은 입력으로 받는다
다이아몬드는 *로 채운다
단 가운데 m 인 부분은 빈칸으로 한다. (m < n)
m도 입력으로 받되 m>=n의 경우 문제가 발생하므로 다시 입력받도록 요청한다.
바깥쪽 군데군데 빛나는 부분을 만든다. (빛나는 모양은 +를 쓴다)
text로 출력하는걸 기본으로 하되 2d list나 numpy arr로 작성하는 것도 허용
내부 검은 그림자를 만드는게 어려운 분은 m없이 흰색 별만 그리세요


  +  *
    ***
   ***** +
  *** ***
 ***   ***
***     ***
 ***   ***
  *** ***
   *****  +
    ***
     *
n=6
m=3

"""
import numpy as np
import random

n = int(input('n을 입력하세요.'))
m = int(input('m을 입력하세요.'))
s = 3
star_map = [abs(n-i) * [' '] + ['*']*((2*n-1)-abs(2*(n-i))) + abs(n-i)*[' '] if (2*n-1)-abs(2*(n-i))-2*m < 0\
        else abs(n-i) * [' '] + ['*']*m + [' '] * ((2*n-1)-abs(2*(n-i))-2*m) + ['*'] * m + abs(n-i)*[' ']\
        for i in range(1, n*2)]

twinklings = [(i, j) for i in range(2*n-1) for j in range(2*n-1) if (abs(i-5) + abs(j-5)) > 5]
twinklings = random.sample(twinklings, s)
star_map = np.array(star_map)
for twinkling in twinklings:
    star_map[twinkling[0]][twinkling[1]] = '+'

for i in star_map:
    print(''.join(i))





