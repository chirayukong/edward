#!/usr/bin/env python
"""This demonstrates a more idiomatic TensorFlow example, which
provides more fine-grained experimentation. We do not call
inference.run().  Alternatively, we directly access the TensorFlow
session and manipulate various objects during inference.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import edward as ed
import tensorflow as tf

from edward.models import Normal

ed.set_seed(42)

# MODEL
z = Normal(mu=1.0, sigma=1.0)

# INFERENCE
qz = Normal(mu=tf.Variable(tf.random_normal([])),
            sigma=tf.nn.softplus(tf.Variable(tf.random_normal([]))))

inference = ed.MFVI({z: qz})
inference.initialize(n_iter=250)

init = tf.initialize_all_variables()
init.run()

for _ in range(inference.n_iter):
  info_dict = inference.update()
  inference.print_progress(info_dict)
