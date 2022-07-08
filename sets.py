myset={"apple","banana","cherry"}

for x in myset:
    print(x)

myset.add("Orange")
print(myset)

newset={"pineapples","mango","papaya"}
myset.update(newset)
print(myset)

myset.remove("pineapples")
print(myset)