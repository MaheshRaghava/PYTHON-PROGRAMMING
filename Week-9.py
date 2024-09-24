#Files
f = open('mahesh.txt','w')
f.write("Hello Cutie")
f = open('mahesh.txt','a')
f.write(" cse-c")
f = open('mahesh.txt','r')
print(f.read())
f.seek(5)
pos = f.tell()
print(pos)
f.read(5)
pos = f.tell()
print(pos)
f.close()
#Binary file
f = open('mahesh.txt','wb')
f.write(b'\x00\x01\x03')
f = open('mahesh.bin','rb')
print(f.read())
f.close()
#CSV
import csv
data=[['s.No','RollNo','Name'],
     [1,24,'Cutie'],
     [2,28,'chinnu']]
file=open('table.csv','w',newline='')
w=csv.writer(file)
w.writerows(data)
