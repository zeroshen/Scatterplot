import random
import math
import pandas as pd

# y = ax + b

a = -1
result = ''
outfile = 'xDom,yDom,correlation\n'

xList = []
yList = []
max_y = 50
min_y = 50

for j in range(100):
    result = ''
    outfile = 'xDom,yDom,correlation\n'

    xList = []
    yList = []
    max_y = 50
    min_y = 50
    for i in range(50):
        # x = random.uniform(2, 98)
        x = random.uniform(-98, -2)
        r1 = random.uniform(35, 55)
        b = random.uniform(-r1, r1)
        y = a * x + b
        if y > max_y:
            max_y = y
        
        if y < min_y:
            min_y = y

        xList.append(x)
        yList.append(y)




    xTrans = pd.Series(xList)
    yTrans = pd.Series(yList)
    cor = round(xTrans.corr(yTrans), 3)
    print(xTrans.corr(yTrans))
    print(cor)

    # if -0.495 > cor > -0.505:
    #     break

    if -0.745 > cor > -0.755:
        break

new_yList = []
for i in yList:
    new_y = (i - min_y)/(max_y-min_y) * 95 + 3
    new_yList.append(new_y)

xTrans2 = pd.Series(xList)
yTrans2 = pd.Series(new_yList)
cor2 = round(xTrans2.corr(yTrans2), 3)
print(xTrans2.corr(yTrans2))
print(cor2)

for i in range(50):
    result += (f'\t{"{"}x: {xList[i]}, y:{new_yList[i]}, correlation: {a}, {"}"},\n')
    outfile += (f'{xList[i]}, {new_yList[i]}, {a}\n')

f = open("output.txt", "w")
f.write(result)
f.close()

f2 = open("t4-d-(" + str(cor) +").csv", "w")
f2.write(outfile)
f2.close()

# a = -1
# result = ''
# outfile = 'xDom,yDom,correlation\n'

# xList = []
# yList = []

# for i in range(50):
#     x = random.uniform(-5, -95)
#     r1 = random.uniform(20, 25)
#     b = random.uniform(-r1, r1)
#     y = a * x + b

#     xList.append(x)
#     yList.append(y)

#     result += (f'\t{"{"}x: {x}, y:{y}, correlation: {a}, {"}"},\n')
#     outfile += (f'{x}, {y}, {a}\n')
