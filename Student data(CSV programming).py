import csv as c
a = open("data.csv","w")
write = c.writer(a)
write.writerow(["Student name","Class","Section","Totalmarks"])

ho = int(input("How many inputs do you want to give :"))

for i in range(ho):
    na = str(input("Enter student name :"))
    cl = str(input("Enter class :"))
    se = str(input("Enter section :"))
    ma = int(input("Enter total marks :"))
    print("*"*50)
    x = [na,cl,se,ma]
    write.writerow(x)

a.close()
