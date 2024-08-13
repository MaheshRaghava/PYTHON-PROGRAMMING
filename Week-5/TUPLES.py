
#CONCATENATION
l1=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input("Enter the element:"))
    l1.append(ele)
print("l1=",l1)
t1=tuple(zip(l1))
print("t1=",t1)
l2=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input("Enter the element:"))
    l2.append(ele)
print("l2=",l2)
t2=tuple(zip(l2))
print("t2=",t2)
print("t1+t2=",t1+t2)
#FINDING INDEX
l = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input("Enter the element: "))
    l.append(ele)
print("l =", l)
t = tuple(l)
print("t =", t)
m = int(input("Enter an element to find its index: "))
if m in t:
    print("Index of the element is:", t.index(m))
else:
    print("Element not found in the tuple.")
#FINDING LENGTH
l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input("Enter the element:"))
    l.append(ele)
print("l=",l)
t=tuple(zip(l))
print("t=",t)
print("length of tuple=",len(t))
#COUNT
l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input("Enter the element:"))
    l.append(ele)
print("l=",l)
t=tuple(zip(l))
print("t=",t)
m=int(input("Enter an element:"))
print(t.count(m))
#REPETITION
l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input("Enter the element:"))
    l.append(ele)
print("l=",l)
t=tuple(zip(l))
print("t=",t)
m=int(input("Enter repetion number:"))
print(t*m)
#ZIP OPERATION
l1=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input("Enter the element:"))
    l1.append(ele)
print("l1=",l1)
t1=tuple(zip(l1))
print("t1=",t1)
l2=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input("Enter the element:"))
    l2.append(ele)
print("l2=",l2)
t2=tuple(zip(l2))
print("t2=",t2)
t3=tuple(zip(t1,t2))
print(t3)

