A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [1, 2, 3, 4, 5, 6, 7, 8, 10]

def exercisefive(List1, List2):
    if (len(List1) != len(List2)):
        return None
    
    for i in range(len(List1)):
        if List1[i] != List2[i]:
            return False
    
    return True

print(exercisefive(A, B))


