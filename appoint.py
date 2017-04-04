# -*- coding:utf-8 -*-‘’
'''
一个项目分ABCD四部分，甲乙丙丁完成各部分时长都不相同，四人都要参与且每人只一项任务，如何指派使项目最快完成，5x5/6x6/7x7....
'''
import random
import numpy as np

def test(numpy_):
    for i in range(len(numpy_)):
        new_np = [item - min(numpy_[i]) for item in numpy_[i]]
        numpy_[i] = new_np

    for i in range(len(numpy_)):
        min_num = 1000000000
        for j in range(len(numpy_[i])):
            if int(numpy_[j, i]) < min_num:
                min_num = numpy_[j, i]
        if min_num == 0:
            continue
        for j in range(len(numpy_[i])):
            numpy_[j, i] -= min_num
    while True:
        zero_exist = True
        while zero_exist:
            zero_exist = False
            if row_appoint(numpy_):
                zero_exist = True
            if col_appoint(numpy_):
                zero_exist = True
        if is_best(numpy_):
            break

        update_d(numpy_)

        for i in range(len(numpy_)):
            for j in range(len(numpy_)):
                if numpy_[i, j] < 0:
                    numpy_[i, j] = 0
    return numpy_

def row_appoint(numpy_):
    zero_exist = False
    for i in range(len(numpy_)):
        zero_count = 0
        col_index = -1
        for j in range(len(numpy_)):
            if numpy_[i, j] == 0:
                zero_count += 1
                col_index = j
                zero_exist = True
        if zero_count == 1:
            numpy_[i, col_index] = -1
            for k in range(len(numpy_)):
                if k == i:
                    continue
                elif numpy_[k, col_index] == 0:
                    numpy_[k, col_index] = -2
        elif zero_count == 2:
            if random.random() > 0.95:
                numpy_[i, col_index] = -1
                for k in range(len(numpy_)):
                    if k == i:
                        continue
                    elif numpy_[k, col_index] == 0:
                        numpy_[k, col_index] == -2
                for j in range(len(numpy_)):
                    if j == col_index:
                        continue
                    elif numpy_[i, j] == 0:
                        numpy_[i, j] = -2
    return zero_exist

def col_appoint(numpy_):
    zero_exist = False
    for j in range(len(numpy_)):
        zero_count = 0
        row_index = -1
        for i in range(len(numpy_)):
            if numpy_[i, j] == 0:
                zero_count += 1
                row_index = i
                zero_exist = True
        if zero_count == 1:
            numpy_[row_index, j] == -1
            for k in range(len(numpy_)):
                if k == j:
                    continue
                elif numpy_[row_index, k] == 0:
                    numpy_[row_index, k] = -2
    return zero_exist

def is_best(numpy_):
    count = 0
    for i in range(len(numpy_)):
        for j in range(len(numpy_)):
            if numpy_[i, j] == -1:
                count += 1
    return count == len(numpy_)

def update_d(numpy_):
    row_is_checked = [False] * (len(numpy_))
    col_is_checked = [False] * (len(numpy_))
    for i in range(len(numpy_)):
        for j in range(len(numpy_)):
            if numpy_[i, j] == -1:
                row_is_checked[i] = False
                break
            else:
                row_is_checked[i] = True
    is_checked = True
    while is_checked:
        is_checked = False
        for i in range(len(numpy_)):
            if row_is_checked[i]:
                for j in range(len(numpy_)):
                    if numpy_[i, j] == -2 and not col_is_checked[j]:
                        col_is_checked[j], is_checked = True, True
        for j in range(len(numpy_)):
            if col_is_checked[j]:
                for i in range(len(numpy_)):
                    if numpy_[i, j] == -1 and not row_is_checked[i]:
                        row_is_checked[i], is_checked = True, True
    min_num = 10000
    for i in range(len(numpy_)):
        if row_is_checked[i]:
            for j in range(len(numpy_)):
                if not col_is_checked[j]:
                    if numpy_[i, j] < min_num:
                        min_num = numpy_[i, j]
    for i in range(len(numpy_)):
        if row_is_checked[i]:
            for j in range(len(numpy_)):
                if numpy_[i, j] > 0:
                    numpy_[i, j] -= min_num
    for j in range(len(numpy_)):
        if col_is_checked[j]:
            for i in range(len(numpy_)):
                if numpy_[i, j] > 0:
                    numpy_[i, j] += min_num

def printResult(numpy_):
    print '---------------Results----------------'
    for i in range(len(numpy_)):
        for j in range(len(numpy_)):
            if numpy_[i, j] == -1:
                print (i + 1), '号员工完成', (j + 1), '号任务；'

if __name__ == '__main__':
    numpy_ = np.array([[5, 9, 3, 6, 7], [2, 7, 4, 1, 2], [3, 8, 5, 9, 6], [4, 6, 2, 7, 5], [6, 5, 7, 4, 8]])
    numpy_ = test(numpy_)
    printResult(numpy_)
