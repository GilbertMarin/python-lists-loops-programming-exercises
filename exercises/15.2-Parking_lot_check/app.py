parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(matriz):
    state = {
        'total_slots': 0,
        'available_slots': 0,
        'occupied_slots': 0
    }

    for row in range(len(matriz)):
        for col in range(len(matriz)):

            if matriz[row][col] != 0:

                state['total_slots'] += 1

                if matriz[row][col] == 1:
                    state['occupied_slots'] += 1
                else:
                    state['available_slots'] += 1

    return state

print(get_parking_lot(parking_state))