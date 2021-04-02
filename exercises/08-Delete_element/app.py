people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_List = []
    for x in range(len(people)):
        if (people[x]!= person_name):
            new_List.append(people[x])
    return new_List        
    
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))