"""
문제 2 : 행맨 (Hang man) (중)
'rabbit'을 단어라고 한다.
철자의 개수만큼 _를 만든다.
시작할 때 목숨은 바꿀 수 있게하되 기본은 5개이다.
글자를 맞추면 해당하는 위치의 _가 글자로 바뀐다.
맞추지 못하면 life를 하나 깍는다.
모음은 (A, E, I, O, U)는 잘 못 적어도 life를 깍지 않는다.
문제의 아래쪽에는 이때까지 시도한 글자가 뜬다
life 이내에 다 맞추면 성공 메세지가 뜨고 실패하면 실패 메세지가 뜬다.

_abb__
your try : a, k, b, o
life : ***

please input a word : t

_abb_t
your try : a, k, b, o, t
life : ***
"""

life = int(input('life를 입력하세요.'))


