import random
import math

center_x = 50
center_y = 50
radius = 35

# x = random.uniform(0, 15)
# y = math.sqrt((1.5 * radius) ** 2 - (center_x - x) ** 2) + center_y
# print(f'\t{"{"}x: {x}, y:{y}, status: false, {"}"},')

# x2 = random.uniform(85, 100)
# y2 = center_y - math.sqrt((1.525 * radius) ** 2 - (center_x - x2) ** 2)
# print(f'\t{"{"}x: {x2}, y:{y2}, status: true, {"}"},\n')

#-----------------------------------------------------------------------
# x = random.uniform(85, 100)
# y = math.sqrt((1.5 * radius) ** 2 - (center_x - x) ** 2) + center_y
# print(f'\t{"{"}x: {x}, y:{y}, status: false, {"}"},')

# x2 = random.uniform(0, 15)
# y2 = center_y - math.sqrt((1.525 * radius) ** 2 - (center_x - x2) ** 2)
# print(f'\t{"{"}x: {x2}, y:{y2}, status: true, {"}"},')

#-----------------------------------------------------------------------
x = random.uniform(0, 15)
y = center_y - math.sqrt((1.5 * radius) ** 2 - (center_x - x) ** 2)
print(f'\t{"{"}x: {x}, y:{y}, status: false, {"}"},')

x2 = random.uniform(85, 100)
y2 = center_y + math.sqrt((1.525* radius) ** 2 - (center_x - x2) ** 2)
print(f'\t{"{"}x: {x2}, y:{y2}, status: true, {"}"},\n')

#-----------------------------------------------------------------------
# x = random.uniform(85, 100)
# y = center_y - math.sqrt((1.5 * radius) ** 2 - (center_x - x) ** 2)
# print(f'\t{"{"}x: {x}, y:{y}, status: false, {"}"},')

# x2 = random.uniform(0, 15)
# y2 = center_y + math.sqrt((1.525 * radius) ** 2 - (center_x - x2) ** 2)
# print(f'\t{"{"}x: {x2}, y:{y2}, status: true, {"}"},')

# basic-1.5
# l1-2.0 
# l2-1.9
# l3-1.8
# l4-1.75
# l5-1.7
# l6-1.65
# l7-1.6
# l8-1.575
# l9-1.55
# l10-1.525


# Task 2
# basic-100
# l1-50/150
# l2-60/140
# l3-70/130
# l4-80/120
# l5-85/115
# l6-90/110
# l7-92/108
# l8-94/106
# l9-96/104
# l10-98/102

# basic-1.5
# l5-1.7
# l6-1.65
# l7-1.6
# l8-1.575
# l9-1.55
# l10-1.525

# Task 2
# basic-100
# l1-50/150
# l2-60/140
# l3-70/130
# l4-80/120
# l5-85/115
# l6-90/110
# l7-92/108
# l8-94/106
# l9-96/104
# l10-98/102

# basic-1.5
# l1-1.7
# l2-1.675
# l3-1.65
# l4-1.625
# l5-1.6
# l6-1.575
# l7-1.55
# l8-1.525

# 1.5125, 1.5735
