import random
import math
import pandas as pd

# y = ax + b

a = 1
result = ''
outfile = 'xDom,yDom,tendency\n'

xList = []
yList = []

for i in range(50):
    r0 = random.uniform(40, 95)
    x = random.uniform(5, r0)
    r1 = random.uniform(15, 20)
    b = random.uniform(-r1, r1)
    y = a * x + b

    xList.append(x)
    yList.append(y)
    
    result += (f'\t{"{"}x: {x}, y:{y}, tendency: {a}, {"}"},\n')
    outfile += (f'{x}, {y}, {a}\n')

xTrans = pd.Series(xList)
yTrans = pd.Series(yList)
print(xTrans.corr(yTrans))

f = open("output.txt", "w")
f.write(result)
f.close()

f2 = open("t3-l5-d2-" + str(a) +".csv", "w")
f2.write(outfile)
f2.close()
