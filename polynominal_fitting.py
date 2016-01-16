import tensorflow as tf
import numpy as np
import random

x = np.float32(np.random.rand(50))
b = 2
# sin(2 * pi * x) + b
y = np.sin(2 * np.pi * x) + b
print x
print y


# create model
w3 = tf.Variable(random.random(), name="w3")
w2 = tf.Variable(random.random(), name="w2")
w1 = tf.Variable(random.random(), name="w1")
w0 = tf.Variable(random.random(), name="w0")

model_y = w3*np.power(x,3) + w2*np.power(x,2) + w1*x + w0


loss = tf.reduce_sum(0.5 * tf.square(model_y - y))
learn_weight = 0.01
optimizer = tf.train.GradientDescentOptimizer(learn_weight)
train = optimizer.minimize(loss)


def record_summary():
    w3_summary = tf.scalar_summary("weight 3", w3)
    w2_summary = tf.scalar_summary("weight 2", w2)
    w1_summary = tf.scalar_summary("weight 1", w1)
    w0_summary = tf.scalar_summary("weight 0", w0)
    loss_summary = tf.scalar_summary("loss", loss)
    m = tf.merge_summary([w3_summary, w2_summary, w1_summary, w0_summary, loss_summary]) 
    return m

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    writer = tf.train.SummaryWriter("data", graph_def=sess.graph_def)    
    sess.run(init_op)

    for step in range(0, 1000):
        sess.run(train)
        summary_str = sess.run(record_summary())
        writer.add_summary(summary_str, step)
        print step, sess.run(w3), sess.run(w2), sess.run(w1), sess.run(w0)

