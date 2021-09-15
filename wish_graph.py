import statistics
import random
import os
import pickle
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

total_c6_counts = []
total_r5_new_counts = []
limited_character_roll = []
limited_weapon_roll =[]
character_roll = []
weapon_roll = []

def plot_c6():
    plot_min = 0
    plot_max = 1200
    plot_range = range(plot_min, plot_max)
    
    plt.figure(num=1, figsize=[12.8,4.8])
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.hist(x=total_c6_counts, bins=plot_range)
    plt.xlabel('# Rolls')
    plt.ylabel('Frequency')
    plt.title("# Rolls to C6")
    plt.xticks(np.arange(plot_min, plot_max, 50))

    plt.savefig(fname="graph_c6.jpg")
    return

def plot_r5():
    plot_min = 0
    plot_max = 1200
    plot_range = range(plot_min, plot_max)

    plt.figure(num=2, figsize=[12.8,4.8])
    plt.ticklabel_format(useOffset=False, style='plain') 
    plt.hist(x=total_r5_new_counts, bins=plot_range)
    plt.xlabel('# Rolls')
    plt.ylabel('Frequency')
    plt.title("# Rolls to R5")
    plt.xticks(np.arange(plot_min, plot_max, 50))

    plt.savefig(fname="graph_r5.jpg")
    return

def plot_limited_character():
    plot_min = 0
    plot_max = 250
    plot_range = range(plot_min, plot_max)

    plt.figure(num=3, figsize=[12.8,4.8])
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.hist(x=limited_character_roll, bins=plot_range)
    plt.xlabel('# Rolls')
    plt.ylabel('Frequency')
    plt.title("# Rolls to Limited Character")
    plt.xticks(np.arange(plot_min, plot_max, 20))
    
    plt.savefig(fname="graph_limited_character.jpg")
    return

def plot_limited_weapon():
    plot_min = 0
    plot_max = 250
    plot_range = range(plot_min, plot_max)
    
    plt.figure(num=4, figsize=[12.8,4.8])
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.hist(x=limited_weapon_roll, bins=plot_range)
    plt.xlabel('# Rolls')
    plt.ylabel('Frequency')
    plt.title("# Rolls to Limited Weapon")
    plt.xticks(np.arange(plot_min, plot_max, 20))

    plt.savefig(fname="graph_limited_weapon.jpg")
    return

def plot_any_character():
    plot_min = 0
    plot_max = 100
    plot_range = range(plot_min, plot_max)

    plt.figure(num=5, figsize=[12.8,4.8])
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.hist(x=character_roll, bins=plot_range)
    plt.xlabel('# Rolls')
    plt.ylabel('Frequency')
    plt.title("# Rolls to Any 5 Star Character")
    plt.xticks(np.arange(plot_min, plot_max, 10))

    plt.savefig(fname="graph_any_character.jpg")
    return

def plot_any_weapon():
    plot_min = 0
    plot_max = 100
    plot_range = range(plot_min, plot_max)

    plt.figure(num=6, figsize=[12.8,4.8])
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.hist(x=weapon_roll, bins=plot_range)
    plt.xlabel('# Rolls')
    plt.ylabel('Frequency')
    plt.title("# Rolls to Any 5 Star Weapon")
    plt.xticks(np.arange(plot_min, plot_max, 10))

    plt.savefig(fname="graph_any_weapon.jpg")
    return

if __name__ == '__main__':
    #matplotlib.use('TkAgg')

    with open('dataset_c6.pkl', 'rb') as f:
        total_c6_counts = pickle.load(f)
    
    with open('dataset_r5.pkl', 'rb') as f:
        total_r5_new_counts = pickle.load(f)
    
    with open('dataset_limited_character.pkl', 'rb') as f:
        limited_character_roll = pickle.load(f)

    with open('dataset_limited_weapon.pkl', 'rb') as f:
        limited_weapon_roll = pickle.load(f)
    
    with open('dataset_any_character.pkl', 'rb') as f:
        character_roll = pickle.load(f)

    with open('dataset_any_weapon.pkl', 'rb') as f:
        weapon_roll = pickle.load(f)

    plot_c6()
    plot_r5()
    plot_limited_character()
    plot_limited_weapon()
    plot_any_character()
    plot_any_weapon()

    plt.show()
