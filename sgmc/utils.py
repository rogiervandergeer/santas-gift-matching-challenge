

def siblings(child_id):
    if child_id > 45000:
        return child_id, 
    elif child_id <= 5000:
        return tuple(child_id - child_id%3 + i for i in range(3))
    else:
        return tuple(child_id - (child_id-1)%2 + i for i in range(2))   
    
    