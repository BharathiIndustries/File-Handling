import csv as c
x = open("GST_rate_calulator.csv","w")
write = c.writer(x)
write.writerow(["Product Name","Rate","GST %","Final product rate"])

do = "y"
while do == "y":
    a= int(input("How many product entries do you want to make :"))

    for i in range(a):
        na = str(input("Enter product name :"))
        ra = int(input("Enter rate of product :"))
        gs = int(input("Enter GST persentage :"))
        print("*"*50)
        fi = ra + ((ra*gs)/100)
        lis = [na,ra,gs,fi]
        write.writerow(lis)
    do = str(input("Do you want to add more entries(y/n) :"))

x.close()
print("The CSV file is ready")
