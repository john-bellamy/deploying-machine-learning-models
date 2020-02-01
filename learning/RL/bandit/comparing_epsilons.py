import numpy as np
import matplotlib.pyplot as plt

class Bandit:
  """m is true  mean"""
  def __init__(self, m):
    self.m = m
    self.mean = 0
    self.N = 0

  def pull(self): #explore; Gaussian
    return np.random.randn() + self.m

  def update(self, x):
    self.N += 1
    self.mean = (1 - 1.00/self.N) * self.mean + 1.0/self.N * x

