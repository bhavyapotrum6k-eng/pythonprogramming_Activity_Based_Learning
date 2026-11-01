# Case 28 - Repeated Transaction
ids = ["T101", "T102", "T101", "T103", "T102"]
amounts = [500, 1000, 500, 2000, 10000]

print("All transactions:", ids)

# find duplicates using list
suspicious = []
for i in range(len(ids)):
    if ids.count(ids[i]) > 1 and ids[i] not in suspicious:
        suspicious.append(ids[i])
    if amounts[i] > 5000: # threshold violation
        print(f"High amount: {ids[i]} - {amounts[i]}")

print("Duplicate IDs:", suspicious)