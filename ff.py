import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
iris =datasets.load_iris()
x_vals=np.array([x[0:4] for x in iris.data])
y_vals=np.array([y for y in iris.target])

y_vals=y_vals.reshape(150,1)


#creating placeholders and setting up trainng rate
learning_rate=0.05

x_data=tf.placeholder(shape=[150,4],dtype=tf.float32)
y_target=tf.placeholder(shape=[150,1],dtype=tf.float32)
a=tf.Variable(tf.random_normal(shape=[4,3]))
b=tf.Variable(tf.random_normal(shape=[3]))
sess=tf.Session()
#logistic algorithm
model_output=tf.add(tf.matmul(x_data,a),b)
loss=tf.nn.l2_loss(model_output-y_target,name="squared_error_cost")
init=tf.global_variables_initializer()
print(sess.run(init))

my_opt=tf.train.GradientDescentOptimizer(0.01)
train_step=my_opt.minimize(loss)
prediction=tf.round(tf.sigmoid(model_output))

residuals=model_output-y_target


with tf.Session() as sess:
    # Step 7: initialize the necessary variables
    sess.run(tf.global_variables_initializer())
    writer=tf.summary.FileWriter('./graphs', sess.graph)

    print(sess.graph)
    #summary_writer = tf.train.SummaryWriter("logistic_logs/", graph_def=sess.graph_def)




#residuals=model_output-y_target

    for i in range(1500):
        _,train_loss=sess.run([train_step,loss],
        feed_dict={x_data:x_vals,y_target:y_vals})
    writer.close()
