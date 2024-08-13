#sum and average
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
print(l)
add=sum(l)
avg=(add)/len(l)
print("sum=",add)
print("avg=",avg)
#Reverse alist
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
print(l[::-1])
#method 2
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
l.reverse()
print(l)
#first occurence
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
m=len(l)-1
t=l[0]
l[0]=l[m]
l[m]=t
print(l)
#method 2
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
ind1=int(input("enter index 1="))
ind2=int(input("enter index 2="))
t=l[ind1]
l[ind1]=l[ind2]
l[ind2]=t
print(l)
#remove
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
for i in range(n):
	for j in range(i+1,n):
		if(l[i]==l[j]):
			remove(l[i])
print(l)
#correct
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
print("Enter element to remove")
m=int(input())
l.remove(m)
print(l)
# even or odd
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
even=[]
odd=[]
for i in range(n):
	if(l[i]%2==0):
		even.append(l[i])
	else:
		odd.append(l[i])
print(even)
print(odd)
#max and min pos
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
print("pos of max=",l.index(max(l)))
print("pos of min=",l.index(min(l)))
