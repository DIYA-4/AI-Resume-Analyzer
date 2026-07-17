list = list(map(int, input("Enter numbers:").split()))

pos = []
neg = []

for i in list:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)

print("Positive: ", pos)
print("Negative: ", neg)        