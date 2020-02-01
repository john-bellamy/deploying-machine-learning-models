import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
from strategies.run_zipline import run_strategy

def  main():
    print("Sample Bot")
    perf = run_strategy('')
    perf.to_csv('report.csv')


if __name__ == '__main__':
    main()