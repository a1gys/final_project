import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

BASES = ["A", "G", "C", "T", "U"]

def gc_ratio(sequence: str) -> float:
    '''Function to calculate the gc-content in percentage in the given string of sequence
    
    Parameters: sequence -> string of bases

    Return: gc-content value in percentage
    '''
    base_count = {}

    for base in BASES:
        counter = sequence.count(base)
        base_count[base] = counter

    return (base_count["C"] + base_count["G"]) / sum(base_count.values()) * 100

def gc_ratio_plot(genom: str, step: int = 100):
    '''Function to plot gc-content distribution for the given genom sequence and saves it as a .png file

    Parameters: genom -> string of bases (for better plot, the length should be large)
                step -> width of a bin (default set to 100)
    
    Return: dictionary of computed values divided into groups, where each length of each group equals to step,
    except the last one, if the sequence modulo step is not equal to 0
    '''
    sequences = {}
    flag = False
    if len(genom) % step == 0:
        flag = True
    
    for i in range(0, len(genom), step):
        sequence = genom[i:i+step]
        computed_gc_ratio = gc_ratio(sequence)
        sequences[i] = computed_gc_ratio

    position = 0
    if flag:
        position = np.arange(len(genom)//step) * step
    else:
        position = np.arange(len(genom)//step+1) * step
        plt.plot(position, sequences.values())
    plt.xlabel('Genom position')
    plt.ylabel('GC-content(%)')
    plt.title('GC-content distribution')
    plt.savefig("gc_content_plot.png")

    return sequences