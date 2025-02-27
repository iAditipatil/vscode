#list to tuple tuple to list
ls=[1,2,3,4,5]
tp=(6,7,8,9,0)

print("list=",ls)
print("tuple=",tp)

tp1=tuple(ls)
ls1=list(tp)

print(tp1)
print(ls1)

add1=ls+list(tp)
print(add1)

add2=tp+tuple(ls)
print(add2)
