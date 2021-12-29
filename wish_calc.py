#Python 3.7

import pandas as pd
import os
import statistics
import traceback
from datetime import datetime

limited_5_star=["Venti", "Klee", "childe", "Zhongli", "Albedo", "Ganyu", "Xiao", "Hu Tao", "Eula", "Kaedehara Kazuha", "Kamisato Ayaka", "Yoimiya", "Raiden Shogun"]

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


limited_5_star_weapons_old=[["2020-11-10", "2020-11-29", 1, "Memory of Dust"],
                            ["2020-12-01", "2020-12-22", 2, "Vortex Vanquisher", "The Unforged"],
                            ["2020-12-22", "2021-01-11", 1, "Summit Shaper"],
                            ["2021-02-02", "2021-02-22", 1, "Primordial Jade Cutter"],
                            ["2021-03-02", "2021-03-17", 1, "Staff of Homa"],
                            ["2021-03-15", "2021-04-05", 1, "Elegy for the End"],
                            ["2021-04-27", "2021-05-17", 2, "Memory of Dust", "Summit Shaper"],
                            ["2021-05-18", "2021-05-31", 1, "Song of Broken Pines"],
                            ["2021-06-31", "2021-07-18", 1, "Freedom-Sworn"]]
limited_5_star_weapons_new=[["2021-07-20", "2021-08-09", 1, "Mistsplitter Reforged"],
                            ["2021-08-09", "2021-08-31", 1, "Thundering Pulse"],
                            ["2021-08-31", "2021-09-20", 2, "Engulfing Lightning", "The Unforged"]]

def gather_5_star_character_stats(filename):

    #file = pd.read_excel(open("paimonmoe_wish_history.xlsx", 'rb'), sheet_name="Character Event", engine="openpyxl")
    file = pd.read_excel(open(filename, 'rb'), sheet_name="Character Event", engine="openpyxl")
    
    #print(file)

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
    for index, row in file.iterrows():
        if row["Banner"] != current_banner:
            current_banner = row["Banner"]
            char_copies = 0
            limited_pity_counter = 0

            temp_any_character_4_star_character_counts = 0
            temp_limited_character_4_star_character_counts = 0
            temp_c6_4_star_character_counts = 0

            temp_any_character_4_star_weapon_counts = 0
            temp_limited_character_4_star_weapon_counts = 0
            temp_c6_4_star_weapon_counts = 0
            
            temp_limited_character_5_star_counts = 0
            temp_c6_5_star_counts = 0

        if row['⭐'] == 5:
            char_name = row['Name']
            # print(row['Name'], " ", row["#Roll"])

            temp_limited_character_5_star_counts += 1
            temp_c6_5_star_counts += 1

            character_roll.append(row["Pity"])
            any_character_4_star_character_counts.append(temp_any_character_4_star_character_counts)
            any_character_4_star_weapon_counts.append(temp_any_character_4_star_weapon_counts)
            temp_any_character_4_star_character_counts = 0
            temp_any_character_4_star_weapon_counts = 0

            if char_name in limited_5_star:
                char_copies += 1

                limited_pity_counter += row["Pity"]
                limited_character_roll.append(limited_pity_counter)
                limited_pity_counter = 0

                limited_character_4_star_character_counts.append(temp_limited_character_4_star_character_counts)
                limited_character_4_star_weapon_counts.append(temp_limited_character_4_star_weapon_counts)
                temp_limited_character_4_star_character_counts = 0
                temp_limited_character_4_star_weapon_counts = 0

                limited_character_5_star_counts.append(temp_limited_character_5_star_counts)
                temp_limited_character_5_star_counts = 0

                if char_copies == 7:
                    c6_counts.append(row["#Roll"])
                    char_copies = 0

                    c6_4_star_character_counts.append(temp_c6_4_star_character_counts)
                    c6_4_star_weapon_counts.append(temp_c6_4_star_weapon_counts)
                    temp_c6_4_star_character_counts = 0
                    temp_c6_4_star_weapon_counts = 0

                    c6_5_star_counts.append(temp_c6_5_star_counts)
                    temp_c6_5_star_counts = 0
            else:
                limited_pity_counter += row["Pity"]
        elif row['⭐'] == 4:
            if row['Type'] == "Character":
                temp_any_character_4_star_character_counts += 1
                temp_limited_character_4_star_character_counts += 1
                temp_c6_4_star_character_counts += 1
            else:
                temp_any_character_4_star_weapon_counts += 1
                temp_limited_character_4_star_weapon_counts += 1
                temp_c6_4_star_weapon_counts += 1

    #print(c6_counts)
    return c6_counts

def gather_5_star_new_weapon_stats(filename):

    #file = pd.read_excel(open("paimonmoe_wish_history.xlsx", 'rb'), sheet_name="Character Event", engine="openpyxl")
    file = pd.read_excel(open(filename, 'rb'), sheet_name="Weapon Event", engine="openpyxl")

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
    # just compute new r5 for now
    for index, row in file.iterrows():
        row_time = datetime.fromisoformat(row["Time"])
        
        # Sanity check for array size
        if current_banner_index >= len(limited_5_star_weapons_new):
            break
        
        # Skip this row if the time is before new banner time
        if row_time < datetime.fromisoformat(limited_5_star_weapons_new[0][0]):
            continue

        # If our time is greater than current banner time, increment banner and reset counts
        while row_time > datetime.fromisoformat(limited_5_star_weapons_new[current_banner_index][1]):
            current_banner_index += 1
            if current_banner_index >= len(limited_5_star_weapons_new):
                break
            r5_copies_1 = 0
            r5_copies_2 = 0
            limited_pity_counter = 0

            temp_any_weapon_4_star_character_counts = 0
            temp_limited_weapon_4_star_character_counts = 0
            temp_r5_4_star_character_counts = 0

            temp_any_weapon_4_star_weapon_counts = 0
            temp_limited_weapon_4_star_weapon_counts = 0
            temp_r5_4_star_weapon_counts = 0

            temp_limited_weapon_5_star_counts = 0
            temp_r5_5_star_counts = 0
        
        if current_banner_index >= len(limited_5_star_weapons_new):
                break
        
        if row['⭐'] == 5:
            weapon_name = row['Name']
            #print(row['Name'], " ", row["#Roll"])

            weapon_roll.append(row["Pity"])

            temp_limited_weapon_5_star_counts += 1
            temp_r5_5_star_counts += 1  

            any_weapon_4_star_character_counts.append(temp_any_weapon_4_star_character_counts)
            any_weapon_4_star_weapon_counts.append(temp_any_weapon_4_star_weapon_counts)
            temp_any_weapon_4_star_character_counts = 0
            temp_any_weapon_4_star_weapon_counts = 0

            # Since so far all the new weapon banners has only 1 limited weapon, we just pick that
            if weapon_name in limited_5_star_weapons_new[current_banner_index][3]:
                r5_copies_1 += 1

                limited_pity_counter += row["Pity"]
                limited_weapon_roll.append(limited_pity_counter)
                limited_pity_counter = 0

                limited_weapon_4_star_character_counts.append(temp_limited_weapon_4_star_character_counts)
                limited_weapon_4_star_weapon_counts.append(temp_limited_weapon_4_star_weapon_counts)
                temp_limited_weapon_4_star_character_counts = 0
                temp_limited_weapon_4_star_weapon_counts = 0

                limited_weapon_5_star_counts.append(temp_limited_weapon_5_star_counts)
                temp_limited_weapon_5_star_counts = 0

                if r5_copies_1 == 5:
                    r5_counts.append(row["#Roll"])
                    r5_copies_1 = 0

                    r5_new_4_star_character_counts.append(temp_r5_4_star_character_counts)
                    r5_new_4_star_weapon_counts.append(temp_r5_4_star_weapon_counts)
                    temp_r5_4_star_character_counts = 0
                    temp_r5_4_star_weapon_counts = 0

                    r5_new_5_star_counts.append(temp_r5_5_star_counts)
                    temp_r5_5_star_counts = 0
            else:
                limited_pity_counter += row["Pity"]
        elif row['⭐'] == 4:
            if row['Type'] == "Character":
                temp_any_weapon_4_star_character_counts += 1
                temp_limited_weapon_4_star_character_counts += 1
                temp_r5_4_star_character_counts += 1
            else:
                temp_any_weapon_4_star_weapon_counts += 1
                temp_limited_weapon_4_star_weapon_counts += 1
                temp_r5_4_star_weapon_counts += 1

    #print(r5_counts)
    return r5_counts

def get_paimon_moe_character_data():
    cwd = os.getcwd()
    for filename in os.listdir(cwd + "/xlsx"):
        if filename.endswith(".xlsx"):
            print(filename)
            try:
                total_c6_counts.extend(gather_5_star_character_stats("xlsx/" + filename))
            except:
                print("Error with file ", filename)
                print(traceback.format_exc())

def get_paimon_moe_weapon_new_data():
    cwd = os.getcwd()
    for filename in os.listdir(cwd + "/xlsx"):
        if filename.endswith(".xlsx"):
            print(filename)
            try:
                total_r5_new_counts.extend(gather_5_star_new_weapon_stats("xlsx/" + filename))
            except:
                print("Error with file ", filename)
                print(traceback.format_exc())


if __name__ == '__main__':
    get_paimon_moe_character_data()
    get_paimon_moe_weapon_new_data()


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



# Cost of 1 roll is $1.98