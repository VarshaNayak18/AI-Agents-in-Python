# Model-Based Agent

environment = {
    "A": "Dirty",
    "B": "Clean"
}

location = "A"

if environment[location] == "Dirty":
    print("Cleaning room A")
    environment[location] = "Clean"