def step(x, y):
    
    remainder = y - x

    if remainder <= 2:
        return remainder
    
    else:
        return step_remainder(remainder)            

def step_remainder(remainder):
        count = 1
        step_count = 1
        remainder = remainder - step_count

        if remainder <= 2:
            count += 2
            return count
        else:
             step_count += 1
             remainder = remainder - step_count
             count += 1
             if remainder <= 2:
                  step_count -= 1
                  remainder = remainder - step_count
                  count += 1
                  if remainder == 0:
                       return count
                  else:
                       remainder - step_count
                       count += 1
                       return count
          

