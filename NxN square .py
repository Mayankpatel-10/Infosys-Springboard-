N = int(input("Enter N: "))

num = 1
for i in range(N):
    # Loop through columns
    for j in range(N):
        print(num, end=" ")
        num += 1
    print() 
