'''
  m is a nynum array[[],[],[]]
@author: zluo
'''
import matplotlib.pyplot as plt
import numpy as np

def scatter_features(m): 
    execute(index_scatter, m)

def plot_features(m): 
    execute(index_plot, m)

def execute(plot_func, m):
        rows = m.shape[0]
        
        for i in range(rows):
            for j in range(i+1,rows):
                 plot_func(i, j, m)
            if (i+1 < rows):     
                plt.legend()
                plt.show()

def index_plot(x, y, m):
    plt.plot(m[x], m[y], label = get_label(x,y))

def index_scatter(x, y, m):
    plt.scatter(m[x], m[y], color = get_color(y), marker = get_maker(y), label = get_label(x,y))
    
def _plot(x, y):
    plot_features(np.vstack((x, y)))
                  
def _scatter(x, y):
    scatter_features(np.vstack((x, y)))
   
markers =['d','+', 'o', 'x', 's','p','h','8','^','>','<']
colors = ['r','b','g','c','m','y','k']

def get_color(j):
    return colors[j % len(colors)]
    
def get_maker(j):
    return markers[j % len(markers)]

def get_label(i, j):  
    return 'F(' + str(i) +  ',' + str(j) + ')'
        