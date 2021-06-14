import numpy as np 

def can_see_stage(seating_arrangement):
    # seating_arrangement = np.array([[1, 3, 5],
    #                        [6, 2, 8], 
    #                        [9, 4, 1]])

    seating_arrangement = np.array(seating_arrangement)
    
    print(seating_arrangement.shape)
    transposed_arragnement = np.transpose(seating_arrangement)

    # print(transposed_arragnement[0])
    
    for col in transposed_arragnement:
        print(col)
        if all(x <= y for x,y in zip(col, col[1:])):
            pass
        else:
            return False;

    return True

print(can_see_stage(input()))

# [[1,2,3], [4,5,6], [7,8,9]]

# TO DO:
# - pass array to command line