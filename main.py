import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def graph_tot(fich):
    f = open(fich, 'r')
    a = f.readlines()
    counts = []
    raman = []
    for x in a:
        ele = x.split(',')
        raman.append(float(ele[1]))
        counts.append(float(ele[2]))

    plt.plot(raman, counts)
    plt.xlabel('Raman shift')
    plt.ylabel('Counts')
    plt.show()


def graph_zero(fich):
    f = open(fich, 'r')
    a = f.readlines()
    counts = []
    raman = []
    counts2 = []
    raman2 = []
    for x in a:
        ele = x.split(',')
        raman.append(float(ele[1]))
        counts.append(float(ele[2]))
    ens = list(zip(raman, counts))

    for x in ens:
        if x[0] >= 0:
            raman2.append(x[0])
            counts2.append(x[1])

    plt.plot(raman2, counts2)
    plt.xlabel('Raman shift')
    plt.ylabel('Counts')
    plt.show()

def écart_type(fich):
    f = open(fich, 'r')
    a = f.readlines()
    counts = []
    raman = []
    for x in a:
        ele = x.split(',')
        raman.append(float(ele[1]))
        counts.append(float(ele[2]))
    print(np.std(counts))

def show_peaks(fich, promi):
    '''Paramètre promi sert à trouver les pics, plus il augmente plus le pic doit être proéminent pour être affiché'''
    f = open(fich, 'r')
    a = f.readlines()
    counts = []
    raman = []
    counts2 = []
    raman2 = []
    for x in a:
        ele = x.split(',')
        raman.append(float(ele[1]))
        counts.append(float(ele[2]))
    ens = list(zip(raman, counts))
    for x in ens:
        if x[0] >= 0:
            raman2.append(x[0])
            counts2.append(x[1])
    raman2 = np.array(raman2)
    counts2 = np.array(counts2) 
    ens2 = list(zip(raman2, counts2))
    points_maxi = []
    b = find_peaks(counts2, prominence=promi)
    for x in b[0]:
        points_maxi.append(ens2[int(x)])
    for x in points_maxi:
        plt.plot(x[0], x[1], 'o', color = 'red')
    for x in points_maxi:
        plt.text(x[0], x[1]+0.5, '({}, {})'.format(x[0], x[1]))
    plt.plot(raman2, counts2)
    plt.show()
    print(points_maxi)

écart_type('huile_olive_100s.TXT')
graph_zero('huile_olive_100s.TXT')
graph_tot('huile_olive_100s.TXT')
show_peaks('huile_olive_100s.TXT', 1800)


