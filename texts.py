import sys

filef = open(sys.argv[1], "r")
x = 0

for line in filef:
    f = open(str(x), "w")
    f.write(line)
    f.close()
    x = x+1
