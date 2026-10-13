
fruits = "apple banana sev apple mirchi jackfruit"

d = {}

for j in fruits.split():
    if j in d:
        d[j] += 1
    else:
        d[j] = 1

print(d)
print(d.keys())
print(d.values())