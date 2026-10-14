L=eval(input("Enter the grades of the student : "))
n=input("Enter the grade (A-F) you want to count : ")
c=0
flag=0
for i in L:
    if i.upper()==n.upper():
        c+=1
        flag=1
print("The number of times ",n," occured = ",c)
if flag==0:
    print("The grade ",n," is not found")
