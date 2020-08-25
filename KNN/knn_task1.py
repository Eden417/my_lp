# coding:utf-8
from collections import Counter


def get_lab(x=[18, 90]):
    data = [[2, 100], [99, 5], [101, 10], [3, 104], [98, 2], [1, 81]]
    label = ['R', 'A', 'A', 'R', 'A', 'R']
    dist = []
    for i in range(len(data)):
        dist.append(((data[i][0] - x[0]) ** 2 + (data[i][1] - x[1]) ** 2) ** 0.5)
    k = 3
    dist_k = dist[:k]
    md = max(dist[:k])
    label_k = label[:k]
    for i in dist[k:]:
        if i < md:
            label_k.remove(label_k[dist_k.index(md)])
            dist_k.remove(md)
            dist_k.append(i)
            label_k.append(label[dist.index(i)])
            md = max(dist_k)
            # print(md)
    # print(label_k)
    # print(dist_k)
    results = Counter(label_k)
    for k, v in results.items():
        if v == max(results.values()):
            return k


if __name__ == '__main__':
    print(get_lab())
