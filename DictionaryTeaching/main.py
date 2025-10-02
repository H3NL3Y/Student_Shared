datavalues = "Alice 12345 Bob 67890 Charlie 13579 Diana 24680 Alice"
tokens = datavalues.split()
dict = {}

for i in range(0, len(datavalues[-1]), 2):
    name = tokens[i]
    number = tokens[i + 1]
    dict[name] = number

query = tokens[8]

if query in dict:
    print(dict[query])
else:
    print("Name not found.")
