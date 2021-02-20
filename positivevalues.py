NumList = []
Positive = []
j = 0

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    if(NumList[j] >= 0):
        Positive.append(NumList[j])
    j = j + 1

print("Element in Positive List is : ", Positive)
