# main.py - A simple Python script demonstrating basic data structures and functions
# Following PEP 8 guidelines

# 1. Lists
things = ["left shoes", "pasta", "drugs"]
print("Things I might steal at 3 AM:", things)

# 2. Dictionaries
person = {
    "name": "big phil",
    "age": "old enough",
    "hobby": "your mom"
}
print("The duke of nova scotia:", person)

# 3. Tuples
coordinates = (51.5074, -0.1278)  # Random but mysterious
print("Coordinates of buried treasure (probably):", coordinates)

# 4. Loops
print("Considering these things for a heist:")
for thing in things:
    print(thing)

# 5. Functions
def greet(name):
    return f"Hello, {name}! Welcome to jurassic park."

print(greet(person["name"]))

# 6. Mathematical Anomaly
result = (80084 * 2069) + 69
print("Advanced mathematical anomaly reveals:", result)


