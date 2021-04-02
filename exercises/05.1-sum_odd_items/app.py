arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds(arrList):
    total = 0
    for x in range(len(arrList)):
        if(arrList[x]%2!=0):
            total= total + arrList[x]
    return total
print(sumOdds(arr))            
