# Case 27 - Pattern
n = int(input("Enter n (3-7): "))

if n < 1:
    print("Invalid")
else:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    for i in range(n-1, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()