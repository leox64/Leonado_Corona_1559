x = 1

while x <= 100:
    print("La tabla del",x)
    print(18*"=")
    for y in range (1,11):
        print("%s * %s = %s" % (x,y,x*y))

    x += 1