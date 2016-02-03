'''
Created on Feb 2, 2016

@author: zluo
'''
import matplotlib.pyplot as plt
'''
  m is a nynum array[[],[],[]]
'''
def scatter_features(m): 
    print('-----------scatter features----------')
    execute(_scatter, m)

def plot_features(m): 
    print('-----------plot features----------')
    execute(_plot, m)

def execute(func, m):
    len = m.shape[0]
    i = 0
    while i < len :
       li = premature(i, len, m)
       func(i , li)
       i += 1
    
            
def premature(i, len, m): 
    li =[]
    j = i + 1
    while(j < len):
        li.append((m[i],m[j]))
        j += 1
    return li

def _scatter(index, li):
        mk =['d','+', 'o', 'x', '^','>','<', 's','p','h','8','+','x']
        colors = ['r','b','g','c','m','y','k']
        i=index + 1
        for tup in li:
            plt.scatter(tup[0], tup[1], color=colors[i%len(colors)], marker=mk[i% len(mk)], label = 'F(' + str(index) +  ',' + str(i) + ')')
            i += 1
        plt.legend()
        plt.show()
        
def _plot(index, li):
        i=index + 1
        for tup in li:
            plt.plot(tup[0], tup[1], label = 'F(' + str(index) +  ',' + str(i) + ')')
            i += 1
        plt.legend()
        plt.show()
        
        
           
    