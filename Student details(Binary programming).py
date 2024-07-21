x= int(input("Enter the number of student data you want to Enter :"))
file = open("Student_details.dat","w")

for i in range(x):
    na = str(input("Enter student name :"))
    cl = str(input("Enter class :"))
    se = str(input("Enter Section :"))
    ro = str(input("Enter roll number :"))
    print("*"*50)
    n = na+"|"+cl+"|"+se+"|"+ro+"\n"
    file.write(n)

print("The Binary file for data is created")
do = str(input("Do you want to add more data(y/n) :"))
while do == "y":
    na = str(input("Enter student name :"))
    cl = str(input("Enter class :"))
    se = str(input("Enter Section :"))
    ro = str(input("Enter roll number :"))
    print("*"*50)
    n = na+"|"+cl+"|"+se+"|"+ro+"\n"
    file.write(n)
    do = str(input("Do you want to add more data(y/n) :"))
    
if do == "n":
    print("The binary file is ready")

file.close()
