classPython=['andrew','peter','ana']
classWebApp=['andrew','ana','kate']
all=classWebApp+classPython
bothClasses=[]
for i in classPython:
    for j in classWebApp:
        if i==j:
            bothClasses.append(i)
for i in all:
    for j in bothClasses:
        if i==j:
            all.remove(i)
            all.remove(j)
print(" The students who attend both classes are: ", ', '.join(bothClasses))
print (" The students who dont attend both classes are: ", ', '.join(all))
