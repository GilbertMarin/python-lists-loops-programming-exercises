import random

#Create the function below:

# Option 1
def matrixBuilder(num):
    matriz = []

    for row in range(num):
        row = []
        
        for col in range(num):
            row.append(random.randint(1,1))

        matriz.append(row)

    return matriz

print (matrixBuilder(3))