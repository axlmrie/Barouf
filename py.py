import sys 

a = []
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))

del b
print(sys.getrefcount(a))


a.b = b
b.a = a