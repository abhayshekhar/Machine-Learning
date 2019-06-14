import numpy as np
import pandas as pd
from IPython.display import display
import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_dataset = load_iris()
print('Keys of iris_dataset: \n{}'.format(iris_dataset.keys()))
print(iris_dataset['DESCR'][:193]+'\n...')


