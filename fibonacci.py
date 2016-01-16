# -*- coding: utf-8 -*-
# 参照：http://qiita.com/n_kats_/items/252a4cea0dc8eca8f980

import tensorflow as tf

# 更新されうる数値
u = tf.Variable(1, "int64")
v = tf.Variable(0, "int64")

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init_op) # 変数初期化
    print sess.run(v) # sess.run(v)でほしい情報の取得

# u = u + v
# assignで第二引数を第一引数に割り当てる
# update_uは処理
update_u = tf.assign(u, tf.add(u, v)) 
update_v = tf.assign(v, tf.sub(u, v)) 

#  with tf.Session() as sess:の中が処理の単位
#  前に行った処理は全てリセットされる
with tf.Session() as sess:
    sess.run(init_op) # 変数初期化
    for i in range(1, 10):
        sess.run(update_u)
        sess.run(update_v)
        print "iteration: %s" % i
        print "v = %s" % sess.run(v) # sess.run(v)でv取得

