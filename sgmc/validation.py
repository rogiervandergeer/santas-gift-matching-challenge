from .utils import siblings

MAX_CHILD_HAPPINESS = 200
MAX_SANTA_HAPPINESS = 2000


def validate_solution(solution):
    for row in solution:
        for element in row:
            if element <= 45000:
                sib = siblings(element)
                for s in sib:
                    if s not in row:
                        return False
    return True


def total_happiness_from_solution(solution, child_happiness_table, santa_happiness_table):
    """Returns the total happiness, to be used as an intermediate solution."""
    total_child_happiness, total_santa_happiness = 0, 0
    for gift_type_id, childs_ids in enumerate(solution):
        for child_id in childs_ids:
            child_happiness = child_happiness_table[child_id, gift_type_id] - 1
            total_child_happiness += child_happiness
            
            santa_happiness = santa_happiness_table[child_id, gift_type_id] - 1
            total_santa_happiness += santa_happiness
    return total_child_happiness, total_santa_happiness


def score_from_happiness(total_child_happiness, total_santa_happiness, solution):
    """Converts happiness to a score"""
    total_child_happiness, total_santa_happiness = total_happiness
    total_child_happiness /= (solution.size * MAX_CHILD_HAPPINESS)
    total_santa_happiness /= (solution.size * MAX_SANTA_HAPPINESS)
    score = total_child_happiness**3 + total_santa_happiness**3
    return score


def score_solution(solution, child_happiness_table, santa_happiness_table):
    total_child_happiness, total_santa_happiness = total_happiness_from_solution(solution, child_happiness_table, santa_happiness_table)
    score = happiness_to_score(total_child_happiness, total_santa_happiness, solution)
    return score, total_happiness


def _happiness_delta(solution, mutation, happiness_table):
    old_happiness, new_happiness = 0, 0
    for swap in mutation:       
        (gift_type_id, i), (gift_type_id2, i2) = swap
        child_id, child_id2 = solution[gift_type_id, i], solution[gift_type_id2, i2]
        old_happiness += happiness_table[gift_type_id, child_id] + happiness_table[gift_type_id2, child_id2]
        new_happiness += happiness_table[gift_type_id, child_id2] + happiness_table[gift_type_id2, child_id]
    return new_happiness - old_happiness


def score_mutation(solution, total_child_happiness, total_santa_happiness, mutation, child_happiness_table, santa_happiness_table):
    total_child_happiness += _happiness_delta(solution, mutation, child_happiness_table)
    total_santa_happiness += _happiness_delta(solution, mutation, santa_happiness_table)
    score = score_from_happiness(total_child_happiness, total_santa_happiness, solution)
    return score