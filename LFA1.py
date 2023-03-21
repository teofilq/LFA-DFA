d={}
f= open("text.in", 'r')
s=f.readline()
sf = s.split()
s = f.readline()
while s!="":
    s=s.split()
    if s[0] not in d:
        d[s[0]] = {s[1] : s[2]}
    else:
        if s[1] not in d[s[0]]:
            d[s[0]][s[1]] = s[2]
    s = f.readline()
f.close()
x = input("Dati sirul: ")
if x == "":
    dr = ["q0"]
else:
    dr = []
sc = "q0"
for i in x:
    if sc in d:
        if i in d[sc]:
            dr.append(d[sc][i])
            sc = d[sc][i]
        else:
            print("nu")
            break
    else:
        print("nu")
        break
else:
    if dr[len(dr)-1] in sf:
        for i in range (len(dr)-1):
            print(dr[i], end = "->")
        print(dr[len(dr)-1])
    else:
        print("nu")