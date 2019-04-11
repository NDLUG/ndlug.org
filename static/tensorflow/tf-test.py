import sys
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

tf.reset_default_graph()

with tf.name_scope("calculation"):
    x = tf.placeholder(tf.float32, [1])

    z = tf.get_variable(name="z", initializer = 
        tf.random_uniform(shape=[1], minval=1, maxval = 10))

with tf.name_scope("loss-and-optimizer"):
    loss = tf.math.abs(tf.math.subtract(tf.constant(10.0, shape=[1]),
        tf.math.multiply(x, z)))

    optimizer = tf.train.AdamOptimizer(0.1).minimize(loss)

with tf.name_scope("accuracy-section"):
    ref = tf.divide(tf.constant(10.0, shape=[1]), x)
    accuracy = tf.subtract(tf.constant(1.0, shape=[1]),
        tf.divide(tf.math.abs(tf.math.subtract(ref, z)), ref))

init = tf.global_variables_initializer()

z_collection = []
with tf.Session() as session:
  session.run(init)

  nIt = 1000
  step = 1
  while step < nIt:

    if len(sys.argv) > 2:
        writer = tf.summary.FileWriter("./test-tf/" + str(step), session.graph)
        runOptions = tf.RunOptions(trace_level = tf.RunOptions.FULL_TRACE)
        run_metadata = tf.RunMetadata()
        ACC, LOSS, OPT, Z = session.run([accuracy, loss, optimizer, z], feed_dict
            = {x: np.array([float(sys.argv[1])])}, options = runOptions,
            run_metadata=run_metadata)
    else:
        ACC, LOSS, OPT, Z = session.run([accuracy, loss, optimizer, z], feed_dict
            = {x: np.array([float(sys.argv[1])])})

    z_collection.append(z.eval()[0])
    if step % 100 == 0:
        print("Acc: "+str(ACC))
        print("Loss: "+str(LOSS))
        print("Z: "+str(Z))
        print("------------")
    step = step + 1

plt.plot(z_collection)
plt.ylabel('Z Value')
plt.xlabel('Step')
plt.show()