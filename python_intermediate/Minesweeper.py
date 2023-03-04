import numpy as np
from collections import defaultdict
mine_num = np.random.randint(15, 25)
# mine은 'x', mine이 아니면 'o'
mine_map = np.array(['x'] * int(mine_num) + ['o'] * (100 - int(mine_num)))

np.random.shuffle(mine_map)
mine_map = mine_map.reshape(10,10)
# Minemap에 padding
mine_map = np.pad(mine_map, 1, 'constant', constant_values='o')
mine_map_count = np.array([0]*100).reshape(10, 10)
print(mine_map)

for i in range(1, 10):
    for j in range(1, 10):
        # 지뢰가 있으면 -1
        if mine_map[i][j] == 'x':
            mine_map_count[i-1][j-1] = -1
        else:
            # 주변의 지뢰갯수를 세주는 dictionary 생성
            unique, counts = np.unique(mine_map[i-1:i+2, j-1:j+2], return_counts=True)
            uniq_dict = dict(zip(unique, counts))
            if not ('x' in uniq_dict.keys()):
                mine_map_count[i-1][j-1] = 0
            else:
                mine_map_count[i-1][j-1] = uniq_dict['x']

print(mine_map_count)






