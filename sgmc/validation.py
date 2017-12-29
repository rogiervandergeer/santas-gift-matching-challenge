from .utils import siblings


def validate_solution(solution):
    for row in solution:
        for element in row:
            if element <= 45000:
                sib = siblings(element)
                for s in sib:
                    if s not in row:
                        return False
    return True


def score_solution(solution, happiness_table):
    """Returns the score of an initial solution"""
    total_happiness = 0
    for gift_type_id, childs_ids in enumerate(solution):
        for child_id in childs_ids:
            happiness = happiness_table[gift_type_id, child_id] + 1
            total_happiness += happiness
    return total_happiness


def update_score(score, solution, mutation, happiness_table):
    """Returns the score from a score
    
    Example
    score = 100
    mutation = ((0,1), (1,1))
    
    new_score = update_score(score, solution, mutation, happiness_table)
    """
    (gift_type_id, i), (gift_type_id2, i2) = mutation
    child_id, child_id2 = solution[gift_type_id, i], solution[gift_type_id2, i2]
    old_happiness = happiness_table[gift_type_id, child_id] + happiness_table[gift_type_id2, child_id2]
    new_happiness = happiness_table[gift_type_id, child_id2] + happiness_table[gift_type_id2, child_id]
    return score - old_happiness + new_happiness