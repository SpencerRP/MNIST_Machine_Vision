import pandas as pd, numpy as np, matplotlib.pyplot as plt
from mnist import MNIST
from sklearn.manifold import TSNE
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from time import time
from matplotlib.ticker import NullFormatter
from sklearn.svm import SVC