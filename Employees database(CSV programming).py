import csv as c
x = open("Employee_Data.csv","w")
write = c.writer(x)
write.writerow(["Employee name","Year of joining","Current salary","Increment","tax"])

ho = int(input("How many Enteris do you want to make :")) 

for i in range(ho):
    em = str(input("Enter Employee name :"))
    ye = int(input("Enter Employee Year of joining :"))
    cu = int(input("Enter Employee current salary :"))
    ni = int(input("Enter increment for Employee :"))
    if ni+cu < 50000:
        a = (ni+cu)*0.2
    elif ni+cu > 50000 and ni+cu < 100000:
        a = (ni+cu)*0.3
    elif ni+cu > 100000:
        a = (ni+cu)*0.35
    print("*"*50)
    l = [em,ye,cu,ni,a]
    write.writerow(l)


print("The input data's after adding tax")
print("""For salary
<50000 = 20% tax
>50000 and <100000 = 30% tax
>100000 = 35% tax
""")

x.close()

with open("Employee_Data.csv","r",newline = "\r\n") as re:
    r = c.reader(re)
    for j in r:
        print(j)


