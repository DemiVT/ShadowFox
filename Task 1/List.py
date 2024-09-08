# List of superheroes
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members
print("Number of members in Justice League:", len(justice_league))

# 2. Add new members
justice_league.extend(["Batgirl", "Nightwing"])
print("Updated Justice League:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Updated Justice League:", justice_league)

# 4. Separate Aquaman and Flash, place Green Lantern in between
justice_league.remove("Aquaman")
justice_league.remove("Flash")
justice_league.insert(2, "Aquaman")
justice_league.insert(3, "Flash")
print("Updated Justice League:", justice_league)

# 5. Replace with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)

# 6. Sort alphabetically and print the new leader
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader:", justice_league[0])
