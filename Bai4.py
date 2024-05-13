def create():   
    f = open('test1.txt','w')
    myfile = f.write("Welcome\n")
    myfile = f.write("to\n")
    myfile = f.write("ITPlus\n")
    myfile = f.write("!")
    return myfile
create()
print("")

#a.
def a():
    f = open('test1.txt','r')
    max = ""
    for i in f:
        if len(i) > len(max):
            max = i
    return max
print(a())

#b
def b():
    f = open('test1.txt','w')
    f.write("Welcome to ITPlus !")
    with open('test1.txt', 'r') as f:
        content = f.read()
    return content

print(b(),"\n")



