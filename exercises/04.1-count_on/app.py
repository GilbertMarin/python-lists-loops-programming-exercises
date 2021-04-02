
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello=[]
for x in range(len(my_list)):
    if (type(my_list[x])== dict or type(my_list[x])== list):
        hello.append(my_list[x])

print(hello)
