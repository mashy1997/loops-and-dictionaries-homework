united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
wales = united_kingdom[1]
wales["capital"] = "Cardiff"

print(united_kingdom)

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom = { "name": "Northern Ireland", "capital": "Belfast", "population": "1,811,00" }

print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.

# for name in united_kingdom.values():
#     print(name("name")) 

# 4. Use a loop to find the total population of the UK.
# total_population = 0

# for population in united_kingdom:
#     total_population += population("population")
#     population["population"] = 0

# print(f"{total_population} is the total population of the UK")
# print(int(united_kingdom))