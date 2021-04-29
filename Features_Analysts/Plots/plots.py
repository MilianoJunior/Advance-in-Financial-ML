import numpy as np
import matplotlib.pyplot as plt

class plot():
    
    def __init__(self,name='graficos'):
        self.name = name
        
    def sinal(self,s1,s2,x,y,title=''):
        fig, (ax1) = plt.subplots(1, 1)
        fig.subplots_adjust(hspace=0.5)
        dt = 1
        t = np.arange(0, len(s1), dt)
        ax1.plot(t, s1, t, s2)
        ax1.set_xlim(0, len(s1))
        ax1.set_xlabel(x)
        ax1.set_ylabel(y)
        ax1.set_title(title)
        ax1.grid(True)
        # cxy, f = ax2.csd(s1, s2, 256, 1. / dt)
        # ax2.set_ylabel('CSD (db)')
        plt.show()
    def hist(self,s1,num_bins,x,y,title=''):
        sigma = 15
        fig, ax = plt.subplots()
        mu = 100  # mean of distribution
        n, bins, patches = ax.hist(s1, num_bins, density=True)
        z = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
             np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        ax.plot(bins, z, '--')
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(title)
        
        # Tweak spacing to prevent clipping of ylabel
        fig.tight_layout()
        plt.show()