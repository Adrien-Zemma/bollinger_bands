import matplotlib.pyplot as plt
import numpy as np

# Random test data

def print_graph(lines):
    np.random.seed(19680801)
    all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    labels = ['x1', 'x2', 'x3']
    print(all_data)
    fig, ax = plt.subplots()
    ax.boxplot(all_data,
                vert=True,
                patch_artist=True,
                labels=labels)
    ax.set(xlabel='time (day(s))', ylabel='Money', title='Bollinger band')
    ax.grid()

    plt.show()