

import numpy as np


# 정규화 관계형 데이터베이스에서 중복을 최소화하기 위해 데이터를 구조화 하는 작업
def min_max_scaling(x):
    x_np = np.asarray(x)
    return (x_np - x_np.min()) / (x_np.max() - x_np.min() + 1e-7)  # 1e-7은 0으로 나누는 오류 예방차


list_test = [0, 1, 2, 3]

test_numpy = np.array(list_test)

print(test_numpy)
print(test_numpy.min())
print(test_numpy - 1)