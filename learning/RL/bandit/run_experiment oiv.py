import numpy as np
import random
import matplotlib.pyplot as plt 
from comparing_epsilons import Bandit 

def run_experiment(m1, m2, m3, oiv, N):
  bandits = [Bandit(m1, oiv), Bandit(m2, oiv), Bandit(m3, oiv)]
  data = np.empty(N)

  for i in range(N):
   
    j = np.argmax([b.mean for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)
    data[i] = x
  
  cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

  plt.plot(cumulative_average)
  plt.plot(np.ones(N) * m1)
  plt.plot(np.ones(N) * m2)
  plt.plot(np.ones(N) * m3)
  plt.xscale('log')
  plt.show()
  for b in bandits:
      print(b.mean)
  return cumulative_average

if __name__ == '__main__':
  c_1 = run_experiment(1.0, 2.0, 3.0, 10, 100000) 
  c_05 = run_experiment(1.0, 2.0, 3.0, 15, 100000) 
  c_01 = run_experiment(1.0, 2.0, 3.0, 5, 100000) 
    
  # log scale plot

  plt.plot(c_1, label='eps=.1')
  plt.plot(c_05, label='eps=.05')
  plt.plot(c_01, label='eps=.01')
  plt.ylim(bottom=0.5, top=3)  
  
  plt.legend()
  plt.xscale('log')
  plt.show()

  # linear plot
    

  plt.plot(c_1, label='eps=0.1')
  plt.plot(c_05, label='eps=0.05')
  plt.plot(c_01, label='eps=0.01')
  plt.legend()
  plt.show()

