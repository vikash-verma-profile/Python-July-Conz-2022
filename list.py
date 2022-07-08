


thislist=["asdasd 1","asdasd 2","asdasd 1",1,2,True]
thislist.append("Orange")
thislist.insert(1,"Apple")

print(thislist)
print(thislist[0])
print(len(thislist))
print("==================================================")
for x in thislist:
    print(x)
print("==================================================")
for i in range(len(thislist)):
    print(thislist[i])
print("====================While loop==============================")
j=0
while j<len(thislist):
    print(thislist[j])
    j=j+1