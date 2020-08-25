# KNN的步骤

1. 算测试数据到训练样本的距离保存到list：**dist **

2. 将训练样本对应标签保存到list：**label**

> 按照数据的距离排序

3. 取出**dist**前**k**个生成list：**dist_k**,取得dist_k的最大距离**md**，label前k个生成list：**label_k**

4. 将dist中k项后的遍历，如果哪一项的值小于md，就将dist_k中最大项替换为该项，同时替换相应的label 项，并且md修改为当前dist_k 最大值

5. 遍历完成后，dist_k 中保存距离最近的k项，label_k中保存相应的标签，计算label_k中最多的标签，为测试数据的标签



