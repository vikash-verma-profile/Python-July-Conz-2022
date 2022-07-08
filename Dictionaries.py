thisdict={
    "1":"Vikash Verma 1 ",
     "2":"Vikash Verma 2 ",
      "3":"Vikash Verma 3",
}

print(thisdict)
print(thisdict["2"])
thisdict["4"]="Vikash Verma 4"
print(thisdict)
thisdict.update({"4":"Ram Kumar"})
print(thisdict)
thisdict.pop("1")
print(thisdict)
thisdict.popitem()
print(thisdict)