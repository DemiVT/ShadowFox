# 1. Calculate BMI Category
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

# 2. Determine the country of a city
cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city = input("Enter a city name: ")
found = False
for country, city_list in cities.items():
    if city in city_list:
        print(f"{city} is in {country}")
        found = True
        break

if not found:
    print("City not found in the list")

# 3. Check if two cities belong to the same country
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = None
country2 = None

for country, city_list in cities.items():
    if city1 in city_list:
        country1 = country
    if city2 in city_list:
        country2 = country

if country1 and country2:
    if country1 == country2:
        print("Both cities are in", country1)
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not found")
