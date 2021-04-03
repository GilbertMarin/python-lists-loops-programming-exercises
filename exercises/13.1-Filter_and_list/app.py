
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def r_filter(names):
    for x in names:
        if (x[0]=="R"):
            return x
resulting_names = list(filter(r_filter, all_names))
print(resulting_names)




