p=[1,2,3]
q=p
print(id(p))
print(id(q))
p.append(4)
print(id(p))
print(id(q))
print(p)
print(q)
a=2
b=a
print(id(a))
print(id(b))
a=3
print(id(a))
print(id(b))
print(a)
print(b)