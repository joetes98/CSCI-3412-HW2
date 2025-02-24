import matplotlib.pyplot as plt
import pandas as pd

def main():

    d = {'Insertion Sort': [0.021, 2.345, 240.403, 1821.183, 8069.402, 39616.518],
         'Merge Sort': [0.003, 0.039, 0.482, 1.525, 3.011, 6.714] }
    
    d2 = {'Insertion Sort': [246373, 224982755, 2505219319, 15644804958, 62475643455, 249925868109],
         'Merge Sort': [1982, 19979, 199962, 499977, 999983, 1999969] }
    
    rowLabels = [1000, 10000, 100000, 250000, 500000, 1000000]
    df = pd.DataFrame(data = d)
    df.index = rowLabels

    df2 = pd.DataFrame(data = d2)
    df2.index =  rowLabels

    print(df2.to_html())

if __name__ == '__main__':
    main()