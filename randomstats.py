#Module Import
import statfunc
from matplotlib import pyplot as plt

#Create List
lst, lowerbound, upperbound, amount = statfunc.createl()

#Finding Mean
print("Your mean is:")
print(statfunc.mean(lst, amount))

#Finding Sum
print("Your sum is:")
print(statfunc.s(lst, amount))

#Finding Median
print("Your median is:")
print(statfunc.median(lst, amount))

#Finding Y
height = []
lst.sort()
for i in range(lowerbound, upperbound+1):
    if (i in lst):
        coun = lst.count(i)
        height.append(coun)

#Establishing X
singleoccurance = []
for i in range(amount):
    if lst[i] not in singleoccurance:
        singleoccurance.append(lst[i])

#Graph Setup
plt.bar(singleoccurance, height, color = 'blue', width = .5)
plt.xticks(lst)
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.title("Frequency of Numbers")

#Graph
print("Your graph is the following:")
plt.show()
