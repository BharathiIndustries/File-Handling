import pickle as p

file = open("Main.txt","r")

read = file.readlines()
for i in range(len(read)):
    x = str(i)
    name = "Sentence_"+x+".txt"
    new = open(name,"wb")
    p.dump(read[i],new)

file.close()

print("Created",len(read)-1,"Number of new binary files")

wh = str(input("Which file do you want to look at :"))
name ="Sentence_"+wh+".txt"
s = ""
nfile = open(name,"rb")
try:
    while True:
        s = p.load(nfile)
        print(s)
except EOFError:
    nfile.close()
