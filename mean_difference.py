# -*- coding: utf-8 -*-
# reduce_meanメソッドの挙動の違い
# 参考: http://stackoverflow.com/questions/34236252/difference-between-np-mean-and-tf-reduce-mean-numpy-tensorflow
import tensorflow as tf

x = [[1.0, 1.0], [2.0, 2.0]]

sess = tf.Session()

# =>  1.5
# (1 + 1 + 2 + 2) / 4
# 全要素に対する平均を出す
print sess.run(tf.reduce_mean(x)) 

# => [1.5, 1.5]
# [ [(1.0 + 2.0) / 2], [(1.0 + 2.0) / 2]]
# 各ベクトルのi次元目毎の平均を出す
print sess.run(tf.reduce_mean(x, 0)) 

# => [1.0,  2.0]
# [ [(1.0 + 1.0) / 2], [(2.0 + 2.0) / 2]]
# 各ベクトルに対する平均を出す
print sess.run(tf.reduce_mean(x, 1)) 
