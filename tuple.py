thistuple=("apple","banana","cheery")
print(thistuple)
print(thistuple[0])
print(thistuple[2:5])
print(thistuple[:2])
print(thistuple[2:])

if "apple" not in  thistuple:
    print("No i dont  have apples")
else:
    print("Yes i have apples")  
print("=====================Update Tuple=============================")
x=("apple","banana","cheery")
y=list(x)
y[1]="KIWI"
x=tuple(y)
print(x)