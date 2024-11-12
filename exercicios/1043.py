entrada = input().split()
a, b, c = map(float, entrada)

if ((a+b) > c and (a+c) > b and (b+c) > a):
    perimetro = a + b + c
    print("Perimetro = {0:.1f}".format(perimetro))
else:
    area = ((a+b) * c)/2
    print("Area = {0:.1f}".format(area))