from random import randint as rnum
#SUM
def s(num, total):
    add = 0
    for i in range(total):
        add += num[i]
    return add

#MEDIAN
def median(num, total):
    num.sort()
    if (total % 2) == 0:
        med = (num[(int(total/2))] + num[int((total/2)-1)])/2
    elif (total % 2) != 0:
        middleindex = int((total / 2))
        med = num[middleindex]
    return med

#COUNTERARRAY: return list (each value represents frequency of index)
#def counter(num, lvalue, mvalue, amnt):
#    counterar = []
#    for i in range(lvalue, mvalue+1):
#        counterar.append(0)
#    for i in range(lvalue, mvalue+1):
#        counterar[i] = num.count(i)
#    return counterar

#MEAN
def mean(num,total):
    sum = 0
    for i in range(total):
        sum += num[i]
    return sum/total

#CREATEDATALIST
def createl():
    print("This program creates random numbers for itself using the random library, and does multiple"
      "operations on them. \nIt takes the upperbound of the range of data from user input, as well as amount of terms.\n\n\n")
    print("Your lower bound for range in this program is automatically set to 0.")
    lowb = int(input("What would you like the lower bound of your range to be?\n"))
    upb = int(input("What would you like the upper bound of your range to be?\n"))
    amnt = int(input("How many values would you like the program to use?\n"))
    list = []
    for i in range(amnt):
        list.append(rnum(lowb,upb))
    print("Your list is:")
    for i in range(amnt):
        print(list[i])
    print("Your list SORTED is:")
    list.sort()
    for i in range(amnt):
        print(list[i])
    return list, lowb, upb, amnt
