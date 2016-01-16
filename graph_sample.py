# -*- coding: utf-8 -*-

# y = x*x のグラフを表示するサンプル

import tensorflow as tf

x = tf.Variable(-100, 'float32')
y = tf.Variable(10000, 'float32')
init = tf.initialize_all_variables()

square_op = tf.assign(x, tf.square(x))
assign_op = tf.assign(y, x)

summary = tf.scalar_summary("y=x*x", tf.to_float(y)) # 第二引数はfloat

with tf.Session() as sess:
    xaxis = range(-100, 100)
    writer = tf.train.SummaryWriter("data", graph_def=sess.graph_def)    
    sess.run(init)
    for i in xaxis:
        sess.run(tf.assign(x, i))
        sess.run(square_op)
        sess.run(assign_op)
        summary_res = sess.run(summary)
        writer.add_summary(summary_res, i)
        print i
        print sess.run(y)





