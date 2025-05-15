Z = []
for i in range (10,30):
    if (i % 2 == 0) and (i % 4 == 0):
        Z.append(str(i))
print (','.join(Z))