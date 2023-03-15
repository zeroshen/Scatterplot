import json
import numpy as np
import matplotlib.pyplot as plt

f = open('T.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# print(json.dumps(data, indent=4))

ratios = ["1:1", "1:2", "2:1", "3:2", "2:3"]

# Task1 -> Level -> Ratio
task1_Correction = [[[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []]]

# Task1 -> Level -> Ratio
task1_Response = [[[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []]]

# Task2 -> Level -> Ratio
task2_Correction = [[[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []]]

# Task2 -> Level -> Ratio
task2_Response = [[[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []]]

# Task3 -> Level -> Ratio
task3_Correction = [[[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []],
                    [[], [], [], [], []]]

# Task3 -> Level -> Ratio
task3_Response = [[[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []]]

task4_Diff = [[], [], [], [], []]
task4_Response = [[], [], [], [], []]


for i in data:
    order = i.split('-')[0]

    if 0 < int(order) < 70:
        level = data[i]['level'] - 1
        ratio = data[i]['ratio']
        correction = data[i]['result']
        response = data[i]['time']
        task1_Correction[level][ratio].append(correction)
        task1_Response[level][ratio].append(response)
    if 100 < int(order) < 199:
        level = data[i]['level'] - 1
        ratio = data[i]['ratio']
        correction = data[i]['result']
        response = data[i]['time']
        task2_Correction[level][ratio].append(correction)
        task2_Response[level][ratio].append(response)
    if 200 < int(order) < 299:
        level = data[i]['level'] - 1
        ratio = data[i]['ratio']
        correction = data[i]['result']
        response = data[i]['time']
        task3_Correction[level][ratio].append(correction)
        task3_Response[level][ratio].append(response)
    if 400 < int(order) < 500:
        correct_value = abs(data[i]['correlationValue'])
        answer = abs(float(data[i]['answer']))
        ratio = data[i]['ratio']
        diff = round(abs(answer - correct_value), 2)
        response = data[i]['time']
        task4_Diff[ratio].append(diff)
        task4_Response[ratio].append(response)


# ---------------------task1-------------------------
# height = [[], [], [], [], []]
# summary = [[], [], [], [], []]
# bars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# for i in range(10):
#     print(i)
#     print(task1_Correction[i])
#     print(task1_Response[i])
#     print("\n\n")
#     for j in range(5):
#         if not task1_Correction[i][j]:
#             height[j].append(0)
#         else:
#             count = 0
#             for k in task1_Correction[i][j]:
#                 summary[j].append(k)
#                 if k == True:
#                     count += 1
#             temp = count/len(task1_Correction[i][j])
#             height[j].append(temp)
#         # barName = ratios[j] + "-" + str(i)
#         # bars.append(barName)
# for i in range(5):
#     plt.clf()
#     y_pos = np.arange(len(bars))
#     title = ratios[i] + " Aspect Ratio Accuracy Rate"
#     plt.title(title)
#     # Create bars
#     plt.bar(y_pos, height[i])
#     # Create names on the x-axis
#     plt.xticks(y_pos, bars)
#     # Show graphic
#     plt.savefig('Task1-Accuracy-' + ratios[i] + '.png')

# summaryBar = []
# for i in range(5):
#     count = 0
#     for k in summary[i]:
#         if k == True:
#             count += 1
#     temp = round(count/len(summary[i]), 2)
#     summaryBar.append(temp)

# plt.clf()
# y_pos = np.arange(len(ratios))
# title = "Aspect Ratio Accuracy Rate Summary"
# plt.title(title)
# # Create bars
# plt.bar(y_pos, summaryBar)
# # Create names on the x-axis
# plt.xticks(y_pos, ratios)
# # Show graphic
# plt.savefig('T1-Accuracy-Summary.png')

# height = [[], [], [], [], []]
# bars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# for i in range(10):
#     print(i)
#     print(task1_Correction[i])
#     print(task1_Response[i])
#     print("\n\n")
#     for j in range(5):
#         if not task1_Response[i][j]:
#             height[j].append(0)
#         else:
#             for k in task1_Response[i][j]:
#                 height[j].append(k)
# plt.clf()
# plt.boxplot(height)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T1-Response-Boxplot.png')

# ---------------------task2-------------------------
# height = [[], [], [], [], []]
# summary = [[], [], [], [], []]
# bars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# for i in range(10):
#     print(i)
#     print(task2_Correction[i])
#     print(task2_Response[i])
#     print("\n\n")
#     for j in range(5):
#         if not task2_Correction[i][j]:
#             height[j].append(0)
#         else:
#             count = 0
#             for k in task2_Correction[i][j]:
#                 summary[j].append(k)
#                 if k == True:
#                     count += 1
#             temp = count/len(task2_Correction[i][j])
#             height[j].append(temp)

# for i in range(5):
#     plt.clf()
#     y_pos = np.arange(len(bars))
#     title = ratios[i] + " Aspect Ratio Accuracy Rate"
#     plt.title(title)
#     # Create bars
#     plt.bar(y_pos, height[i])
#     # Create names on the x-axis
#     plt.xticks(y_pos, bars)
#     # Show graphic
#     plt.savefig('T2-Accuracy-' + ratios[i] + '.png')

# summaryBar = []
# for i in range(5):
#     count = 0
#     for k in summary[i]:
#         if k == True:
#             count += 1
#     temp = round(count/len(summary[i]), 2)
#     summaryBar.append(temp)

# plt.clf()
# y_pos = np.arange(len(ratios))
# title = "Aspect Ratio Accuracy Rate Summary"
# plt.title(title)
# # Create bars
# plt.bar(y_pos, summaryBar)
# # Create names on the x-axis
# plt.xticks(y_pos, ratios)
# # Show graphic
# plt.savefig('T2-Accuracy-Summary.png')

# height = [[], [], [], [], []]
# bars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# for i in range(10):
#     print(i)
#     print(task2_Correction[i])
#     print(task2_Response[i])
#     print("\n\n")
#     for j in range(5):
#         if not task2_Response[i][j]:
#             height[j].append(0)
#         else:
#             for k in task2_Response[i][j]:
#                 height[j].append(k)
# plt.clf()
# plt.boxplot(height)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T2-Response-Boxplot.png')

# ---------------------task3-------------------------
height = [[], [], [], [], []]
summary = [[], [], [], [], []]
bars = ["1", "2", "3", "4", "5", "6", "7"]
for i in range(7):
    print(i)
    print(task3_Correction[i])
    print(task3_Response[i])
    print("\n\n")
    for j in range(5):
        if not task3_Correction[i][j]:
            height[j].append(0)
        else:
            count = 0
            for k in task3_Correction[i][j]:
                summary[j].append(k)
                if k == True:
                    count += 1
            temp = count/len(task3_Correction[i][j])
            height[j].append(temp)
        # barName = ratios[j] + "-" + str(i)
        # bars.append(barName)

# for i in range(5):
#     plt.clf()
#     y_pos = np.arange(len(bars))
#     title = ratios[i] + " Aspect Ratio Accuracy Rate"
#     plt.title(title)
#     # Create bars
#     plt.bar(y_pos, height[i])
#     # Create names on the x-axis
#     plt.xticks(y_pos, bars)
#     # Show graphic
#     plt.savefig('Task3-Accuracy-' + ratios[i] + '.png')

summaryBar = []
for i in range(5):
    count = 0
    for k in summary[i]:
        if k == True:
            count += 1
    temp = round(count/len(summary[i]), 2)
    summaryBar.append(temp)

plt.clf()
y_pos = np.arange(len(ratios))
title = "Aspect Ratio Accuracy Rate Summary"
plt.title(title)
# Create bars
plt.bar(y_pos, summaryBar)
# Create names on the x-axis
plt.xticks(y_pos, ratios)
# Show graphic
plt.savefig('T3-Accuracy-Summary.png')

# height = [[], [], [], [], []]
# for i in range(7):
#     print(i)
#     print(task3_Correction[i])
#     print(task3_Response[i])
#     print("\n\n")
#     for j in range(5):
#         if not task3_Response[i][j]:
#             height[j].append(0)
#         else:
#             for k in task3_Response[i][j]:
#                 height[j].append(k)
# plt.clf()
# plt.boxplot(height)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T3-Response-Boxplot.png')

# ---------------------task4-------------------------
# for i in range(5):
#     print(i)
#     print(task4_Diff[i])
#     print(task4_Response[i])
#     print("\n\n")

# plt.boxplot(task4_Diff)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T4-Diff-Boxplot.png')


# Closing file
f.close()
