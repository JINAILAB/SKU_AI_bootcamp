from typing import Any, Callable, List, Optional, Type, Union
from itertools import permutations
import numpy as np
import copy


class Omok:
    def __init__(self):
        self.map_size = int(input('바둑판의 크기를 자연수로 입력해주세요:'))
        self.board = [['+' for i in range(self.map_size)] for j in range(self.map_size)]
        # 바둑판
        self.count = 0  # 짝수면 흑돌차례 홀수면 백돌차례
        self.board_size = len(self.board[0])
        print('0을 누르면 게임이 종료됩니다. 게임시작!')
        while True:
            if self.play() == 'end':
                break

    def play(self):
        if self.count % 2 == 0:
            while self.count % 2 == 0:
                print('흑돌 순서입니다. 착수해주세요.')
                point = list(map(int, input().split()))  # 흑돌 착수 지점
                if self.check_game_end_byzero(point):  # 0에 의해 게임 끝나는거 check
                    return 'end'
                if self.check_put_error(point):  # 이상한 곳에 두면 다시 두라고 하기
                    continue
                if self.check3x3(point):  # 3x3 체크해주기
                    continue

                self.put_b(point)  # 흑돌 놓기

        elif self.count % 2 == 1:
            while self.count % 2 == 1:
                print('백돌 순서입니다.')
                point = list(map(int, input().split()))
                if self.check_game_end_byzero(point):
                    return 'end'
                if self.check_put_error(point):
                    continue
                if self.check3x3(point):  # 3x3 체크해주기
                    continue
                self.put_w(point)

        if self.check_gameend(point):  # 게임
            if self.count % 2 == 0:
                print('백승')
                return 'end'

            elif self.count % 2 == 1:
                print('흑승')
                return 'end'

        board_list = []
        draw = ''
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

        if (x < 0) or (y < 0) or (x > self.board_size - 1) or (y > self.board_size - 1) or (point == ''):
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
        check1 = [self.board[max(0, x1)][min(len(self.board[0])-1, y1 + i)] for i in range(-4, 5)]
        check2 = [self.board[max(0, x1 + i)][min(self.board[0]-1, y1)] for i in range(-4, 5)]
        check3 = [self.board[max(0, x1 + i)][min(self.board[0]-1, y1 + i)] for i in range(-4, 5)]
        check4 = [self.board[max(0, x1 - i)][min(self.board[0]-1, y1 + i)] for i in range(-4, 5)]
        checks = [''.join(i) for i in [check1, check2, check3, check4]]

        for check in checks:
            if stone_color * 5 in check:
                return True
        return False

    @staticmethod
    def check_game_end_byzero(point):
        if point[0] == 0 and len(point) == 1:
            print('game_end')
            return True

    @staticmethod
    def check_put_error(point):
        if not (len(point) == 2 and isinstance(point[0], int) and isinstance(point[1], int)):
            print('정수 두개를 입력해주세요.')
            return True
        else:
            return False

    def check3x3(self, point):
        x1, y1 = point
        visited = [point]
        direction = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        visited = 





if __name__ == '__main__':
    game = Omok()
