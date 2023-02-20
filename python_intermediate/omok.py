from typing import Any, Callable, List, Optional, Type, Union

map_size = int(input('바둑판의 크기를 자연수로 입력해주세요:'))

omok_board = [['+' for i in range(map_size)] for j in range(map_size)]


class omok:
    def __init__(self, board: List[List[int]]):
        self.board = board  # 바둑판
        self.count = 0  # 짝수면 흑돌차례 홀수면 백돌차례
        self.board_size = len(board[0])

    def play(self):
        if self.count % 2 == 0:
            while self.count % 2 == 0:
                print('흑돌 순서입니다. 착수해주세요.')
                point = list(map(int, input().split()))
                if point[0] == 0 and len(point) == 1:
                    print('game_end')
                    return 'end'
                if not (len(point) == 2 and isinstance(point[0], int) and isinstance(point[1], int)):
                    print('정수 두개를 입력해주세요.')
                    continue
                self.put_b(point)

        elif self.count % 2 == 1:
            while self.count % 2 == 1:
                print('백돌 순서입니다.')
                point = list(map(int, input().split()))
                if point[0] == 0 and len(point) == 1:
                    print('game_end')
                    return 'end'
                if not (len(point) == 2 and isinstance(point[0], int) and isinstance(point[1], int)):
                    print('정수 두개를 입력해주세요.')
                    continue
                self.put_w(point)

        if self.check_gameend(point):
            if self.count % 2 == 0:
                print('백승')
                return 'end'

            elif self.count % 2 == 1:
                print('흑승')
                return 'end'

        board_list = []
        for i in self.board:
            board_list.append(''.join(i))
            draw = ''.join(board_list)
        if not ('+' in draw):
            print('무승부')
            return 'end'

        self.print_board()

    def put_w(self, point: List[int]):
        x, y = point
        if not self.invalid_point([x, y]):
            self.board[x][y] = 'w'
            self.count += 1

    def put_b(self, point: List[int]):
        x, y = point
        if not self.invalid_point([x, y]):
            self.board[x][y] = 'b'
            self.count += 1

    def invalid_point(self, point: List[int]):
        x, y = point

        if (x < 0) or (y < 0) or (x > self.board_size - 1) or (y > self.board_size - 1):
            print('착수 지점이 바둑판 밖입니다. 다시 놓아주세요.')
            return True

        elif (self.board[x][y] == 'w') or (self.board[x][y] == 'b'):
            print('이미 돌이 놓여져있습니다.')
            return True

        else:
            return False

    def print_board(self):
        for i in self.board:
            print(''.join(i))

    def check_gameend(self, point):
        x1, y1 = point
        stone_color = self.board[x1][y1]
        check1 = [self.board[x1][y1 + i] for i in range(-4, 5) if 0 <= y1 + i <= self.board_size - 1]
        check2 = [self.board[x1 + i][y1] for i in range(-4, 5) if 0 <= x1 + i <= self.board_size - 1]
        check3 = [self.board[x1 + i][y1 + i] for i in range(-4, 5) if
                  (0 <= x1 + i <= self.board_size - 1 and 0 <= y1 + i <= self.board_size - 1)]
        check4 = [self.board[x1 - i][y1 + i] for i in range(-4, 5) if
                  (0 <= y1 + i <= self.board_size - 1 and 0 <= x1 - i <= self.board_size - 1)]
        checks = [''.join(i) for i in [check1, check2, check3, check4]]

        for check in checks:
            if stone_color * 5 in check:
                return True
        return False





if __name__ == '__main__':

    game = omok(omok_board)

    print('0을 누르면 게임이 종료됩니다. 게임시작!')
    while True:
        if game.play() == 'end':
            break
