# Martin Kersner, m.kersner@gmail.com
# 2017/06/12

import numpy as np

def zeros_like(list_of_arrays):
 return [np.zeros(l.shape) for l in list_of_arrays]
