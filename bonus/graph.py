import matplotlib.pyplot as plt
import numpy as np

from calc import deviation

# Random test data

def print_graph(lines, standard_dev):
    #print(np.random.normal(0, 1, size=5))
    #all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    datas = []
    for i in range(len(lines)):
        if i == 0:
            datas.append(np.array([lines[i], lines[i]]))
        else:
            datas.append(np.array([lines[i - 1], lines[i]]))
    labels = range(len(lines))
    fig, ax = plt.subplots()
    bplot1 = ax.boxplot(datas,
                vert=True,
                patch_artist=True,
                labels=labels)
    ax.set(xlabel='Index', ylabel='Value', title='Bollinger band')

    for patch, i in zip(bplot1['boxes'], range(len(lines))):
        if i == 0:
            patch.set_facecolor('blue')
        elif lines[i - 1] >= lines[i]:
            patch.set_facecolor('red')
        else:
            patch.set_facecolor('green')

    ax.grid()

    plt.show()