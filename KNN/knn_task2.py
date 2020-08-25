# coding:utf-8
import os
from collections import Counter


# import pandas as pd

def task2():
    path1 = r'C:\Users\eden\Documents\data_823\trainingDigits'
    path2 = r'C:\Users\eden\Documents\data_823\testDigits'
    l1 = os.listdir(path1)
    l2 = os.listdir(path2)
    label = [int(i[0]) for i in l1]
    ges_it = []
    results = []
    # print(label)
    for t in l2:
        with open(path2 + '\\' + t) as f:
            fc = f.read()
        fctl = []
        for i in fc:
            if i.isdigit():
                fctl.append(int(i))
        d = []
        for j in l1:
            with open(path1 + '\\' + j) as f:
                fc = f.read()
            fcal = []
            for i in fc:
                if i.isdigit():
                    fcal.append(int(i))
            d.append(sum([(fctl[p] - fcal[p]) ** 2 for p in range(len(fctl))]) ** 0.5)
        k = 5
        dist_k = d[:k]
        md = max(d[:k])
        label_k = label[:k]
        for i in d[k:]:
            if i < md:
                label_k.remove(label_k[dist_k.index(md)])
                dist_k.remove(md)
                dist_k.append(i)
                label_k.append(label[d.index(i)])
                md = max(dist_k)
        result = Counter(label_k)
        results.append(result)
        # print(result)
        for key, val in result.items():
            if val == max(result.values()):
                ges_it.append(key)
                # print(key)
    co = 0
    try:
        for i in range(len(ges_it)):
            if ges_it[i] == [int(j[0]) for j in l2][i]:
                co += 1
    except IndexError:
        print('最大值存在多个标签，无法决策')
    else:
        print(co / len(ges_it))
        print(ges_it)
        print(results)


if __name__ == '__main__':
    task2()
