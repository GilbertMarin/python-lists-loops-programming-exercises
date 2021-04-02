chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_List = chunk_one
    for x in range(len(chunk_two)):
        new_List.append(chunk_two[x])
    return new_List   
        
    
print(merge_list(chunk_one, chunk_two))
