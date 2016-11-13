import itertools

# Creates a file called algs.txt with all the generated algs

# Examples
# moves = ["R","R'","R2","L","L'","L2","U","U'","U2","B","B'","B2","F","F'","F2","B","B'","B2","M","M'","M2"]
# Using list(itertools.combinations_with_replacement(moves,5)) - Does not account for repeats...
# Another more complete example list...
#moves = ["R","R'","R2","U","U'","U2","F","F'","F2","f","f'","f2","L","L'","L2","D","D'","D2","r","r'","r2","l'","l","l2"]


moves = ["R","R'","R2","U","U'","U2","F","F'","F2"]


ups = ["U","U'","U2"]
downs = ["D","D'","D2",]
rights = ["R","R'","R2","r","r'","r2"]
lefts = ["L","L'","L2","l'","l","l2"]
fronts = ["F","F'","F2","f","f'","f2"]
backs = []

# This creates a list of all combinations of _ moves (including repeats)
# Using the more complete example list, can only go as high as 5 :(
lista = list(itertools.product(moves,repeat=8))
lenlista = len(lista)
print ("Original List: ", lenlista)
f = open ('algs.txt','w')
newlist = []
for alg in lista:
    a = list(alg)
    out = False
    max = len(a)-1
    for i in range(max):
        if a[i][0] in ups:
            if a[i+1][0] in ups:
                out = True
                break
            elif a[i+1][0] in downs:
                if i < max-1:
                    if a[i+2][0] in ups:
                        out = True
                        break
        if a[i][0] in downs:
            if a[i+1][0] in downs:
                out = True
                break
            elif a[i+1][0] in ups:
                if i < max-1:
                    if a[i+2][0] in downs:
                        out = True
                        break

        if a[i][0] in rights:
            if a[i+1][0] in rights:
                out = True
                break
            elif a[i+1][0] in lefts:
                if i < max-1:
                    if a[i+2][0] in rights:
                        out = True
                        break

        if a[i][0] in lefts:
            if a[i+1][0] in lefts:
                out = True
                break
            elif a[i+1][0] in rights:
                if i < max-1:
                    if a[i+2][0] in lefts:
                        out = True
                        break

        if a[i][0] in fronts:
            if a[i+1][0] in fronts:
                out = True
                break
            elif a[i+1][0] in backs:
                if i < max-1:
                    if a[i+2][0] in ups:
                        out = True
                        break
    if (out == False):
        newlist.append(a)

print ("New List: ", len(newlist))
for alg in newlist:
    f.write("".join(alg))
    f.write("\n")
f.close()
