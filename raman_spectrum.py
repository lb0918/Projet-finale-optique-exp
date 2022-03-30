"Fichier qui implémente la classe d'objets raman_spectum qui sert à analyser les spectres raman"
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


class RamanSpectrum:
    def __init__(self, fich, promi):
        self.data = np.genfromtxt(fich, delimiter=',')
        self.raman = self.data[:, 1]
        self.counts = self.data[:, 2]
        self.promi = int(promi)
        self.peaks = self.getPeaks()
        self.name = fich

    def graph(self, peaks=False):
        plt.plot(self.raman, self.counts, label=f'{self.name}')
        if peaks:
            for x in self.peaks:
                plt.plot(x[0], x[1], 'o', color='red')
                plt.text(x[0], x[1] + 0.5, '({}, {})'.format(x[0], x[1]))
        plt.legend()
        plt.xlabel('Raman shift')
        plt.ylabel('Counts')
    def graph_zero(self, peaks=False):
        liste = list(zip(self.raman, self.counts))
        raman = []
        counts = []
        for x in liste:
            if x[0] >= 0:
                raman.append(x[0])
                counts.append(x[1])
        plt.plot(raman, counts, label=f'{self.name}')
        if peaks:
            for x in self.peaks:
                plt.plot(x[0], x[1], 'o', color='red')
                plt.text(x[0], x[1] + 0.5, '({}, {})'.format(x[0], x[1]))
                plt.legend()
                plt.xlabel('Raman shift')
                plt.ylabel('Counts')


    def getPeaks(self):
        promi = self.promi
        ens_ini = list(zip(self.data[:, 1], self.data[:, 2]))
        raman = []
        counts = []
        for x in ens_ini:
            if x[0] >= 0:
                raman.append(x[0])
                counts.append(x[1])
        raman, counts = np.array(raman), np.array(counts)
        ens_fin = list(zip(raman, counts))
        points_maxi = []
        b = find_peaks(counts, prominence=promi)
        for x in b[0]:
            points_maxi.append(ens_fin[int(x)])
        return points_maxi

olive = RamanSpectrum("huile_olive_100s.txt", 1800)
olive.graph(peaks=True)
#olive_1 = RamanSpectrum("huile_olive1.txt")
#olive_1.graph(peaks=True)
plt.show()
olive.graph_zero(peaks=True)
plt.show()