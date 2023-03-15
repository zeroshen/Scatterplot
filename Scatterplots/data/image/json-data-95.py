import json
import numpy as np
import matplotlib.pyplot as plt
import statistics

f = open('Total.json',)
filename = f.name + ".txt"
fw = open(filename, "w")


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
                    [[], [], [], [], []]]

# Task1 -> Level -> Ratio
task1_Response = [[[], [], [], [], []],
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
                    [[], [], [], [], []]]

# Task2 -> Level -> Ratio
task2_Response = [[[], [], [], [], []],
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
                    [[], [], [], [], []]]

# Task3 -> Level -> Ratio
task3_Response = [[[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []],
                  [[], [], [], [], []]]

task4_Diff = [[], [], [], [], []]
task4_Response = [[], [], [], [], []]



for i in data:
    order = i.split('-')[0]
    
    if 0 < int(order) < 99:
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
height = [[], [], [], [], []]
summary = [[], [], [], [], []]
bars = ["1", "2", "3", "4", "5", "6"]
for i in range(6):
    print(i)
    print(task1_Correction[i])
    print(task1_Response[i])
    print("\n\n")
    for j in range(5):
        if not task1_Correction[i][j]:
            height[j].append(-0.001)
        else:
            count = 0
            for k in task1_Correction[i][j]:
                if k == True:
                    count += 1
            temp = round(count/len(task1_Correction[i][j]), 2)
            height[j].append(temp)


for i in range(5):
    for j in range(6):
        fw.write('T1-Accuracy-' + ratios[i] + '-' + str(j) + ': ' + str(height[i][j])+ '\n')
        summary[i].append(height[i][j])

avg = []
std = []
for i in range(5):
    temp = sum(height[i]) / len(height[i])
    avg.append(temp)
    temp = statistics.stdev(height[i])
    std.append(temp)

print(avg)
print(std)

plt.clf()

title =  "Aspect Ratio Accuracy Rate Summary"
plt.title(title)
plt.errorbar([1, 2, 3, 4, 5], avg, xerr=0.5, yerr=2*std, linestyle='')
plt.savefig('T1-Accuracy-Summary.png')


# height = [[], [], [], [], []]
# for i in range(6):
#     print(i)
#     print(task1_Correction[i])
#     print(task1_Response[i])
#     print("\n\n")
#     for j in range(5):
#         for k in task1_Response[i][j]:
#             height[j].append(k)
# plt.clf()
# plt.boxplot(height)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T1-Response-Boxplot.png')

# # ---------------------task2-------------------------
# height = [[], [], [], [], []]
# summary = [[], [], [], [], []]
# bars = ["1", "2", "3", "4", "5", "6"]
# for i in range(6):
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
#             temp = round(count/len(task2_Correction[i][j]), 2) + 0.03
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
# for i in range(6):
#     print(i)
#     print(task2_Correction[i])
#     print(task2_Response[i])
#     print("\n\n")
#     for j in range(5):
#         for k in task2_Response[i][j]:
#             height[j].append(k)
# plt.clf()
# plt.boxplot(height)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T2-Response-Boxplot.png')

# # ---------------------task3-------------------------
# height = [[], [], [], [], []]
# summary = [[], [], [], [], []]
# bars = ["1", "2", "3", "4", "5", "6"]
# for i in range(6):
#     print(i)
#     print(task3_Correction[i])
#     print(task3_Response[i])
#     print("\n\n")
#     for j in range(5):
#         if not task3_Correction[i][j]:
#             height[j].append(0)
#         else:
#             count = 0 
#             for k in task3_Correction[i][j]:
#                 summary[j].append(k)
#                 if k == True:
#                     count += 1
#             temp = round(count/len(task3_Correction[i][j]), 2) + 0.03
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
#     plt.savefig('T3-Accuracy-' + ratios[i] + '.png')

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
# plt.savefig('T3-Accuracy-Summary.png')

# height = [[], [], [], [], []]
# for i in range(6):
#     print(i)
#     print(task3_Correction[i])
#     print(task3_Response[i])
#     print("\n\n")
#     for j in range(5):
#         for k in task3_Response[i][j]:
#             height[j].append(k)
# plt.clf()
# plt.boxplot(height)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T3-Response-Boxplot.png')

# # ---------------------task4-------------------------
# for i in range(5):
#     print(i)
#     print(task4_Diff[i])
#     print(task4_Response[i])
#     print("\n\n")
# plt.clf()
# plt.boxplot(task4_Diff)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T4-Diff-Boxplot.png')

# plt.clf()
# plt.boxplot(task4_Response)
# plt.xticks([1, 2, 3, 4, 5], ratios)
# plt.savefig('T4-Response-Boxplot.png')





# Closing file
f.close()

fw.close()
