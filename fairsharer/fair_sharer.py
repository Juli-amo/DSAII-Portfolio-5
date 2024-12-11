def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in 'values' gives a fraction (share) to both the left and right neighbor. 
    The leftmost field is considered the neighbor of the rightmost field.
    Args:
        values: 1D list of values
        num_iterations: Integer specifying the number of iterations
    """
    if len(values) == 0:
        raise ValueError("The 'values' list cannot be empty.")
    
    for iteration in range(num_iterations):
        highest_value = max(values)
        index = values.index(highest_value)
        shared_piece = highest_value * share
        values[index] = values[index] - 2 * abs(shared_piece)  

        if index == 0:
            values[-1] += abs(shared_piece)  
            values[1] += abs(shared_piece)  
        elif index == len(values) - 1:
            values[0] += abs(shared_piece)  
            values[-2] += abs(shared_piece)  
        else:
            values[index - 1] += abs(shared_piece) 
            values[index + 1] += abs(shared_piece)  
    return values
