# clear()
# del
thislist=["asdasd 1","asdasd 2","asdasd 1",1,2,True]
#thislist.clear();
#del thislist
thislist2=["1","2","3",1,2]
thislist.append("Orange")
#thislist.remove("asdasd 1")
#thislist.pop(3)
thislist.insert(1,"Apple")
thislist.extend(thislist2);
print("=====================New List=============================")
print(thislist)
print("==================================================")
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