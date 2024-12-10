


def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share) to both the left and right neighbor. 
    The leftmost field is considered the neightbor of the rightmost field.
    Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """
    for iteration in range(num_iterations):
        highest_value = max(values)
        index = values.index(highest_value)
        shared_piece = highest_value * share
        values[index] = values[index] - 2*shared_piece
        
        if index == 0:
            values[-1] = values[-1] + shared_piece
            values[1] = values[1] + shared_piece
        elif index == len(values)-1:
            values[0] = values[0] + shared_piece
            values[-2] = values[-2] + shared_piece
        else:
            values[index-1] = values[index-1] + shared_piece
            values[index+1] = values[index+1] + shared_piece
            
    return values