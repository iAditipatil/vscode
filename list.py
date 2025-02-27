#list

f=["apple","mango","banana"]
print("list=",f)

f.append("chikku")
print(f)

f.extend(["berry","gava"])
print(f)

f.insert(2,"jackfruit")
print(f)

print("slice="[1:3])

f.reverse()
print("reverse",f)

f.sort()
print(f)

f.remove("gava")
print(f)

f.pop(2)
print(f)