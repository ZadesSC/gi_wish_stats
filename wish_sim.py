import statistics
import random
import os
import pickle

total_weapon_rolls = 0
total_character_rolls = 0

character_roll = []
weapon_roll = []

limited_character_roll = []
limited_weapon_roll = []

total_c6_counts = []
total_r5_old_counts = []
total_r5_new_counts = []

# Counts for number of 4 stars
any_character_4_star_character_counts = []
any_weapon_4_star_character_counts = []
limited_character_4_star_character_counts = []
limited_weapon_4_star_character_counts = []
c6_4_star_character_counts = []
r5_old_4_star_character_counts = []
r5_new_4_star_character_counts = []

any_character_4_star_weapon_counts = []
any_weapon_4_star_weapon_counts = []
limited_character_4_star_weapon_counts = []
limited_weapon_4_star_weapon_counts = []
c6_4_star_weapon_counts = []
r5_old_4_star_weapons_counts = []
r5_new_4_star_weapon_counts = []

# Counts for number of 5 stars
limited_character_5_star_counts = []
limited_weapon_5_star_counts = []
c6_5_star_counts = []
r5_old_5_star_counts = []
r5_new_5_star_counts = []

def gather_5_star_character_stats():
    global total_character_rolls

    c6_counts = []

    current_banner = ""
    char_copies = 0
    temp_any_character_4_star_character_counts = 0
    temp_limited_character_4_star_character_counts = 0
    temp_c6_4_star_character_counts = 0

    temp_any_character_4_star_weapon_counts = 0
    temp_limited_character_4_star_weapon_counts = 0
    temp_c6_4_star_weapon_counts = 0
    
    temp_limited_character_5_star_counts = 0
    temp_c6_5_star_counts = 0

    limited_pity_counter = 0

    counter_5 = 1
    counter_4 = 1
    counter_roll = 0

    rate_5 = 0.006
    rate_4 = 0.051
    pity_5 = 73
    pity_4 = 8

    hard_pity_flag = False

    # Do simulated rolls until c6
    while char_copies < 7:
        counter_roll += 1
        total_character_rolls += 1

        x = random.uniform(0.0, 1.0)
        prob_5 = rate_5 + max(0, (counter_5 - pity_5) * 10 * rate_5)
        prob_4 = rate_4 + max(0, (counter_4 - pity_4) * 10 * rate_4)

        # We got a 5 star
        if x < prob_5:
            temp_limited_character_5_star_counts += 1
            temp_c6_5_star_counts += 1

            character_roll.append(counter_5)
            any_character_4_star_character_counts.append(temp_any_character_4_star_character_counts)
            any_character_4_star_weapon_counts.append(temp_any_character_4_star_weapon_counts)
            temp_any_character_4_star_character_counts = 0
            temp_any_character_4_star_weapon_counts = 0

            
            soft_pity = random.uniform(0.0, 1.0)

            # We won the 50/50 soft pity
            if hard_pity_flag or soft_pity < 0.5:
                char_copies += 1

                limited_pity_counter += counter_5
                limited_character_roll.append(limited_pity_counter)
                limited_pity_counter = 0

                limited_character_4_star_character_counts.append(temp_limited_character_4_star_character_counts)
                limited_character_4_star_weapon_counts.append(temp_limited_character_4_star_weapon_counts)
                temp_limited_character_4_star_character_counts = 0
                temp_limited_character_4_star_weapon_counts = 0

                limited_character_5_star_counts.append(temp_limited_character_5_star_counts)
                temp_limited_character_5_star_counts = 0

                hard_pity_flag = False

                if char_copies == 7:
                    c6_counts.append(counter_roll)
                    char_copies = 0

                    c6_4_star_character_counts.append(temp_c6_4_star_character_counts)
                    c6_4_star_weapon_counts.append(temp_c6_4_star_weapon_counts)
                    temp_c6_4_star_character_counts = 0
                    temp_c6_4_star_weapon_counts = 0

                    c6_5_star_counts.append(temp_c6_5_star_counts)
                    temp_c6_5_star_counts = 0

                    return c6_counts
            else:
                limited_pity_counter += counter_5
                hard_pity_flag = True
            
            
            counter_5 = 1
            counter_4 += 1
                
        # We got a 4 star        
        elif x < prob_4 + prob_5:
            character_or_weapon = random.uniform(0.0, 1.0)

            # We got a 4 star character
            if character_or_weapon < 0.717:
                temp_any_character_4_star_character_counts += 1
                temp_limited_character_4_star_character_counts += 1
                temp_c6_4_star_character_counts += 1
            # We got a 4 star weapon
            else:
                temp_any_character_4_star_weapon_counts += 1
                temp_limited_character_4_star_weapon_counts += 1
                temp_c6_4_star_weapon_counts += 1
            
            counter_5 += 1
            counter_4 = 1
        
        # We got a 3 star
        else:
            counter_5 += 1
            counter_4 += 1

    #print(c6_counts)
    return c6_counts

def gather_5_star_new_weapon_stats():
    global total_weapon_rolls

    r5_counts = []

    current_banner_index = 0
    r5_copies_1 = 0
    r5_copies_2 = 0

    temp_any_weapon_4_star_character_counts = 0
    temp_limited_weapon_4_star_character_counts = 0
    temp_r5_4_star_character_counts = 0

    temp_any_weapon_4_star_weapon_counts = 0
    temp_limited_weapon_4_star_weapon_counts = 0
    temp_r5_4_star_weapon_counts = 0

    temp_limited_weapon_5_star_counts = 0
    temp_r5_5_star_counts = 0

    limited_pity_counter = 0

    counter_5 = 1
    counter_4 = 1
    counter_roll = 0

    rate_5 = 0.007
    rate_4 = 0.06
    pity_5 = 62
    pity_4 = 7

    hard_pity_flag = False
    eptimoized_path = 0

    # just compute new r5 for now
    while r5_copies_1 < 5:
        counter_roll += 1
        total_weapon_rolls += 1

        x = random.uniform(0.0, 1.0)
        prob_5 = rate_5 + max(0, (counter_5 - pity_5) * 10 * rate_5)
        prob_4 = rate_4 + max(0, (counter_4 - pity_4) * 10 * rate_4)

        if x < prob_5:
            weapon_roll.append(counter_5)

            temp_limited_weapon_5_star_counts += 1
            temp_r5_5_star_counts += 1  

            any_weapon_4_star_character_counts.append(temp_any_weapon_4_star_character_counts)
            any_weapon_4_star_weapon_counts.append(temp_any_weapon_4_star_weapon_counts)
            temp_any_weapon_4_star_character_counts = 0
            temp_any_weapon_4_star_weapon_counts = 0
            
            # 0 <= soft_pity < 0.375 = get main weapon
            # 0.375 <= soft_pity < 0.75 = get off weapon
            # 0.75 <= soft_pity < 1.0 = get standard weapon 
            soft_pity = random.uniform(0.0, 1.0)

            if hard_pity_flag:
                hard_pity_50 = random.uniform(0.0, 1.0)

            if eptimoized_path == 2 or (hard_pity_flag and hard_pity_50 < 0.5) or soft_pity < 0.375:
                r5_copies_1 += 1

                limited_pity_counter += counter_5
                limited_weapon_roll.append(limited_pity_counter)
                limited_pity_counter = 0

                limited_weapon_4_star_character_counts.append(temp_limited_weapon_4_star_character_counts)
                limited_weapon_4_star_weapon_counts.append(temp_limited_weapon_4_star_weapon_counts)
                temp_limited_weapon_4_star_character_counts = 0
                temp_limited_weapon_4_star_weapon_counts = 0

                limited_weapon_5_star_counts.append(temp_limited_weapon_5_star_counts)
                temp_limited_weapon_5_star_counts = 0

                hard_pity_flag = False
                eptimoized_path = 0

                if r5_copies_1 == 5:
                    r5_counts.append(counter_roll)
                    r5_copies_1 = 0

                    r5_new_4_star_character_counts.append(temp_r5_4_star_character_counts)
                    r5_new_4_star_weapon_counts.append(temp_r5_4_star_weapon_counts)
                    temp_r5_4_star_character_counts = 0
                    temp_r5_4_star_weapon_counts = 0

                    r5_new_5_star_counts.append(temp_r5_5_star_counts)
                    temp_r5_5_star_counts = 0

                    return r5_counts

            elif soft_pity < 0.75:
                limited_pity_counter += counter_5
                eptimoized_path += 1
            else:
                limited_pity_counter += counter_5
                eptimoized_path += 1
                hard_pity_flag = True

            counter_5 = 1
            counter_4 += 1

        # We got a 4 star        
        elif x < prob_4 + prob_5:
            character_or_weapon = random.uniform(0.0, 1.0)

            # We got a 4 star character
            if character_or_weapon < 0.178:
                temp_any_weapon_4_star_character_counts += 1
                temp_limited_weapon_4_star_character_counts += 1
                temp_r5_4_star_character_counts += 1
            
            # We got a 4 star weapon
            else:
                temp_any_weapon_4_star_weapon_counts += 1
                temp_limited_weapon_4_star_weapon_counts += 1
                temp_r5_4_star_weapon_counts += 1
            
            counter_5 += 1
            counter_4 = 1

        # We got a 3 star
        else:
            counter_5 += 1
            counter_4 += 1

    #print(r5_counts)
    return r5_counts


def sim_c6(times):
    for index in range(times):
        total_c6_counts.extend(gather_5_star_character_stats())

def sim_r5(times):
    for index in range(times):
        total_r5_new_counts.extend(gather_5_star_new_weapon_stats())


if __name__ == '__main__':

    attemps = 1000000
    sim_c6(attemps)
    sim_r5(attemps)

    with open('dataset_c6.pkl', 'wb') as f:
        pickle.dump(total_c6_counts, f)
    
    with open('dataset_r5.pkl', 'wb') as f:
        pickle.dump(total_r5_new_counts, f)
    
    with open('dataset_limited_character.pkl', 'wb') as f:
        pickle.dump(limited_character_roll, f)

    with open('dataset_limited_weapon.pkl', 'wb') as f:
        pickle.dump(limited_weapon_roll, f)
    
    with open('dataset_any_character.pkl', 'wb') as f:
        pickle.dump(character_roll, f)

    with open('dataset_any_weapon.pkl', 'wb') as f:
        pickle.dump(weapon_roll, f)

    # with open('test.pkl', 'rb') as f:
    #     arr = pickle.load(f)
    # print(arr)

    print("Total C6 Attempts: ", attemps)
    print("Total R5 Attempts: ", attemps)
    print("Total Character Banner Rolls: ", total_character_rolls)
    print("Total Weapon Banner Rolls: ", total_weapon_rolls)
    print("\n\n")


    print("C6 Data")
    #print(total_c6_counts)

    print("Max: ", max(total_c6_counts))
    print("Min: ", min(total_c6_counts))
    print("Average: ", statistics.mean(total_c6_counts))
    print("Median: ", statistics.median(total_c6_counts))
    print("Average # 4 Star Characters: ", statistics.mean(c6_4_star_character_counts))
    print("Average # 4 Star Weapons: ", statistics.mean(c6_4_star_weapon_counts))
    print("Average # 5 Star Character: ", statistics.mean(c6_5_star_counts))
    
    c6_average_dollar_cost = (statistics.mean(total_c6_counts) - (10 * (statistics.mean(c6_5_star_counts) - 1) + 5 * statistics.mean(c6_4_star_character_counts) + 2 * statistics.mean(c6_4_star_weapon_counts)) / 5) * 1.98
    print("Average $ Cost with Starglitter: ", c6_average_dollar_cost)
    print("Average $ Cost without Starglitter: ",  statistics.mean(total_c6_counts) * 1.98)
    print("\n\n")


    print("R5 Data")
    #print(total_r5_new_counts)

    print("Max: ", max(total_r5_new_counts))
    print("Min: ", min(total_r5_new_counts))
    print("Average: ", statistics.mean(total_r5_new_counts))
    print("Median: ", statistics.median(total_r5_new_counts))
    print("Average # 4 Star Character: ", statistics.mean(r5_new_4_star_character_counts))
    print("Average # 4 Star Weapons: ", statistics.mean(r5_new_4_star_weapon_counts))
    print("Average # 5 Star Weapons: ", statistics.mean(r5_new_5_star_counts))

    r5_average_dollar_cost = (statistics.mean(total_r5_new_counts) - (10 * (statistics.mean(r5_new_5_star_counts) - 1) + 5 * statistics.mean(r5_new_4_star_character_counts) + 2 * statistics.mean(r5_new_4_star_weapon_counts)) / 5) * 1.98
    print("Average $ Cost with Starglitter: ", r5_average_dollar_cost)
    print("Average $ Cost without Starglitter: ", statistics.mean(total_r5_new_counts) * 1.98)
    print("\n\n")


    print("Limited Character Data")
    #print(limited_character_roll)

    print("Max: ", max(limited_character_roll))
    print("Min: ", min(limited_character_roll))
    print("Average: ", statistics.mean(limited_character_roll))
    print("Median: ", statistics.median(limited_character_roll))
    print("Average # 4 Star Character: ", statistics.mean(limited_character_4_star_character_counts))
    print("Average # 4 Star Weapon: ", statistics.mean(limited_character_4_star_weapon_counts))
    print("Average # 5 Star Character: ", statistics.mean(limited_character_5_star_counts))
    
    limited_character_average_dollar_cost = (statistics.mean(limited_character_roll) - (10 * (statistics.mean(limited_character_5_star_counts) - 1) + 5 * statistics.mean(limited_character_4_star_character_counts) + 2 * statistics.mean(limited_character_4_star_weapon_counts)) / 5) * 1.98
    print("Average $ Cost with Starglitter: ", limited_character_average_dollar_cost)
    print("Average $ Cost without Starglitter: ", statistics.mean(limited_character_roll) * 1.98)
    print("\n\n")


    print("Limited Weapon Data")
    #print(limited_weapon_roll)

    print("Max: ", max(limited_weapon_roll))
    print("Min: ", min(limited_weapon_roll))
    print("Average: ", statistics.mean(limited_weapon_roll))
    print("Median: ", statistics.median(limited_weapon_roll))
    print("Average # 4 Star Character: ", statistics.mean(limited_weapon_4_star_character_counts))
    print("Average # 4 Star Weapon: ", statistics.mean(limited_weapon_4_star_weapon_counts))
    print("Average # 5 Star Weapon: ", statistics.mean(limited_weapon_5_star_counts))
    

    limited_weapon_average_dollar_cost = (statistics.mean(limited_weapon_roll) - (10 * (statistics.mean(limited_weapon_5_star_counts) - 1) + 5 * statistics.mean(limited_weapon_4_star_character_counts) + 2 * statistics.mean(limited_weapon_4_star_weapon_counts)) / 5) * 1.98
    print("Average $ Cost with Starglitter: ", limited_weapon_average_dollar_cost)
    print("Average $ Cost without Starglitter: ",  statistics.mean(limited_weapon_roll) * 1.98)
    print("\n\n")

    print("Any 5Star Character Data")
    #print(limited_character_roll)

    print("Max: ", max(character_roll))
    print("Min: ", min(character_roll))
    print("Average: ", statistics.mean(character_roll))
    print("Median: ", statistics.median(character_roll))
    print("Average # 4 Star Character: ", statistics.mean(any_character_4_star_character_counts))
    print("Average # 4 Star Weapon: ", statistics.mean(any_character_4_star_weapon_counts))

    any_character_average_dollar_cost = (statistics.mean(character_roll) - (5 * statistics.mean(any_character_4_star_character_counts) + 2 * statistics.mean(any_character_4_star_weapon_counts)) / 5) * 1.98
    print("Average $ Cost with Starglitter: ", any_character_average_dollar_cost)
    print("Average $ Cost without Starglitter: ", statistics.mean(character_roll) * 1.98)
    print("\n\n")


    print("Any 5Star Weapon Data")
    #print(limited_weapon_roll)

    print("Max: ", max(weapon_roll))
    print("Min: ", min(weapon_roll))
    print("Average: ", statistics.mean(weapon_roll))
    print("Median: ", statistics.median(weapon_roll))
    print("Average # 4 Star Character: ", statistics.mean(any_weapon_4_star_character_counts))
    print("Average # 4 Star Weapon: ", statistics.mean(any_weapon_4_star_weapon_counts))
    
    any_weapon_average_dollar_cost = (statistics.mean(weapon_roll) - (5 * statistics.mean(any_weapon_4_star_character_counts) + 2 * statistics.mean(any_weapon_4_star_weapon_counts)) / 5) * 1.98
    print("Average $ Cost with Starglitter: ", any_weapon_average_dollar_cost)
    print("Average $ Cost without Starglitter: ", statistics.mean(weapon_roll) * 1.98)