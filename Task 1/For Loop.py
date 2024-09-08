import random

# 1. Simulate rolling a six-sided die
rolls = [random.randint(1, 6) for _ in range(20)]

count_6 = rolls.count(6)
count_1 = rolls.count(1)
count_2_6s_in_a_row = sum(1 for i in range(1, len(rolls)) if rolls[i] == 6 and rolls[i - 1] == 6)

print("Number of times rolled a 6:", count_6)
print("Number of times rolled a 1:", count_1)
print("Number of times rolled two 6s in a row:", count_2_6s_in_a_row)

# 2. Workout routine
total_jumping_jacks = 100
completed_jumping_jacks = 0

while completed_jumping_jacks < total_jumping_jacks:
    print(f"Perform 10 jumping jacks.")
    completed_jumping_jacks += 10
    tired = input("Are you tired? (yes/no): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            break
    else:
        remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
        print(f"{remaining_jumping_jacks} jumping jacks remaining.")

print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
if completed_jumping_jacks >= total_jumping_jacks:
    print("Congratulations! You completed the workout.")
