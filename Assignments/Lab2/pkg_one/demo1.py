import os

print("hi from demo1")
f1=open("File1.txt",'r')
print(f1.read());
f1=open("File1.txt",'r')
print(f1.read(10));
f1=open("File1.txt",'r')
print(f1.readline());

for i in f1:
    print(i)

f1=open("File1.txt",'w');
f1.write("Hello From Code!");


f1.write(" we b#deen")   
f1.seek(5);
f1.write("old")
f1=open("File1.txt",'a');
f1.write("New")
f1.close();
#-----------------------------------------
os.getcwd  




