my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
var1 = 0
for x in range(len(my_list)):
    var1=var1+my_list[x]
    prom = var1 / float(len(my_list))
print(prom)   
