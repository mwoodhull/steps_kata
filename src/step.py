def step(x, y):
    remainder = y - x  # Distance between x and y
    
    if remainder <= 2:  # If the distance is small (1 or 2), return the remainder directly
        return remainder
    
    count = 1  # Start with the first step of size 1
    step_length = 1  # First step length is 1
    distance_covered = 0  # Track how much distance has been covered
    
    while distance_covered < remainder:
        if distance_covered + step_length + 1 <= remainder:
            # If we can take a larger step, increase step size
            step_length += 1
        else:
            # If we would overshoot, keep the current step length
            step_length = remainder - distance_covered
        
        distance_covered += step_length
        count += 1  # Increment step counter

    return count
