from omok import Omok
import numpy as np
from itertools import permutations
import copy


class Omok3x3(Omok):
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
                if self.check_3x3(point):
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

    def check3x3(self, point):
        print('?????')
        x1, y1 = point
        new_board = self.board
        new_board[x1, y1] = 'n'
        board_with_padding = np.array(new_board)
        board_with_padding = np.pad(new_board, ((1, 1), (1, 1)), 'constant', constant_values=0)
        # 끝자리이면 0 padding 추가
        check1 = [self.board[x1][y1 + i] for i in range(-3, 4) if 0 <= y1 + i <= board_with_padding[0].shape[0] - 1]
        check2 = [self.board[x1 + i][y1] for i in range(-3, 4) if 0 <= x1 + i <= board_with_padding[0].shape[0] - 1]
        check3 = [self.board[x1 + i][y1 + i] for i in range(-3, 4) if
                  (0 <= x1 + i <= board_with_padding[0].shape[0] - 1 and 0 <= y1 + i <= board_with_padding[0].shape[
                      0] - 1)]
        check4 = [self.board[x1 - i][y1 + i] for i in range(-3, 4) if
                  (0 <= y1 + i <= board_with_padding[0].shape[0] - 1 and 0 <= x1 - i <= board_with_padding[0].shape[
                      0] - 1)]
        checks = [''.join(i) for i in [check1, check2, check3, check4]]

        if self.count % 2 == 0:
            my_stone = 'b'
            counter_stone = 'w'

        elif self.count % 2 == 1:
            my_stone = 'w'
            counter_stone = 'b'

        three = ['n', my_stone, my_stone]
        semi_three = ['n', my_stone, my_stone, '+']
        t_per = list(permutations[three])
        f_per = list(permutations[semi_three])
        t_per.extend(f_per)
        all_3x3per = [''.join(i) for i in
                      t_per]  # 3x3종류의 모든 list ['bbn', 'bnb', 'nbb', 'bb+n', 'nbb+', 'n+bb', 'bbn+', '+bbn', 'bnb+', 'bn+b', 'nb+b', 'b+nb', 'b+bn', '+nbb', '+bnb']
        print(' all_3x3per : ', all_3x3per)
        all_3x4pers = []  # 3x4종류의 모든 list
        for i in all_3x3per:
            all_3x4pers.append(i + counter_stone)
            all_3x4pers.append(counter_stone + i)
            all_3x4pers.append(i + '0')
            all_3x4pers.append('0' + i)

        print(' all_3x4per : ', all_3x4pers)

        count3x3_list = []
        for check in checks:
            for per in all_3x3per:
                if per in check:
                    count3x3_list.append((per, check))

        n_count3x3_list = copy.deepcopy(count3x3_list)
        if len(count3x3_list) >= 2:
            for i in count3x3_list:
                id_3x3 = i[1].find(i[0])
                for all_3x4per in all_3x4pers:
                    if (all_3x4per in i[1][id_3x3:id_3x3 + 4]) or (all_3x4per in i[1][id_3x3 - 1:id_3x3 + 3]):
                        n_count3x3_list.remove(i)
        if len(n_count3x3_list) >= 2:
            print('33입니다. 다시 입력해주세요.')
            return True
        else:
            return False


if __name__ == '__main__':
    game = Omok()
