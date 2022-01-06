import statistics
import random
import os
import pickle

rate = 0.005
pity = 60


def sim_s_rank():
    # sim until getting a s rank
    num_roll = 0
    got_copy = 0
    while got_copy == 0:
        num_roll += 1
        if num_roll == 60:
            return 60
        roll =  random.uniform(0.0, 1.0)
        if roll < rate:
            return num_roll

def sim_s_rank_average():
    attempts = 1000000
    rolls = []
    for index in range(attempts):
        num = sim_s_rank()
        rolls.append(num)
    
    average = statistics.mean(rolls)
    print("Average: ", average)


if __name__ == '__main__':
    sim_s_rank_average()