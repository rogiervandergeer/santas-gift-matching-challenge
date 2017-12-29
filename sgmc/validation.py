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
