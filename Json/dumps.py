import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=False)
z = json.dumps(x)

# the result is a JSON string:
print(y)
print(z)