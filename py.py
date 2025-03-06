import sys 

a = []
print(sys.getrefcount(a))


b = a
print(sys.getrefcount(a))


print(sys.getrefcount(a))



a.b = b
b.a = a
a = []
print(sys.getrefcount(b))


b = a
#psdofsdflk


#lfksdjiodsv

