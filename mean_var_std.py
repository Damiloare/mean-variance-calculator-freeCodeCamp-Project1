import numpy as np


def calculate(list):

  if len(list) == 9:

    array1 = np.array(list)
    array = array1.reshape(3, 3)
    #print(array)
    calculations = {
        'mean': [
            np.mean(array, axis=0).tolist(),
            np.mean(array, axis=1).tolist(),
            np.mean(array)
        ],
        'variance': [
            np.var(array, axis=0).tolist(),
            np.var(array, axis=1).tolist(),
            np.var(array.flatten())
        ],
        'standard deviation': [
            np.std(array, axis=0).tolist(),
            np.std(array, axis=1).tolist(),
            np.std(array.flatten())
        ],
        'max': [
            np.max(array, axis=0).tolist(),
            np.max(array, axis=1).tolist(),
            np.max(array.flatten())
        ],
        'min': [
            np.min(array, axis=0).tolist(),
            np.min(array, axis=1).tolist(),
            np.min(array.flatten())
        ],
        'sum': [
            np.sum(array, axis=0).tolist(),
            np.sum(array, axis=1).tolist(),
            np.sum(array.flatten())
        ]
    }
  else:
    raise ValueError('List must contain nine numbers.')
  return calculations


result = calculate([34, 45, 67, 23, 78.456, 786, 23, 56])
print(result)
