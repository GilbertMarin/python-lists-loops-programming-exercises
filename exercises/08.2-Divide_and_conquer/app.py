list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(numb_list):
    even = []
    odd = []
    merged=[]
    for x in range(len(numb_list)):
        if (numb_list[x]%2==0):
            even.append(numb_list[x])
        else:
            odd.append(numb_list[x])  
    merged.append(odd)
    merged.append(even)
    return merged
    
print(merge_two_list(list_of_numbers))

