# A divide-and-conquer algorithm paradigm can solve a large problem by recursively breaking it down into smaller 
# subproblems until they become simple enough to be solved directly.

# Basic- Merge Sort
# Advanced- Matrix Multiplication
# Mindbreaker- Strassen Algorithm

# ____________________________________________EXAMPLES________________________________________________________


# BASIC: MERGE SORT

# 1. SORTING ITERATIVELY WITHOUT USING PYTHON'S BUILT IN SORTED FEATURE
A = [-5, -23, 5, 0, 23, -6, 23, 67]
C = []
while A:
    minimum = A[0]
    for x in A:
        if x < minimum:
            minimum = x
    C.append(minimum)
    A.remove(minimum)
print(C)


# 2. EXPLAINING THE CONCEPT - BASIC (MERGING TWO LISTS - DIVIDING INTO TWO, CONQUERING EACH, MERGING BACK)
def merging(left, right):
    C = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C

left = [2, 5, 6, 10]
right = [3, 4, 12, 20]
print(merging(left, right))


# 3. SORTING RECURSIVELY - TOP DOWN
def sortArray(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = sortArray(A[:middle])
    right = sortArray(A[middle:])
    merged = []
    while left and right:
        if left[0] <= right [0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged
print(sortArray(A))


# 4. SORTING ITERATIVELY WITHOUT USING PYTHON'S BUILT IN SORTED FEATURE - BOTTOM UP
def sortArray(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = A[:mid]
    left_sorted = []
    while left:
        minimum = left[0]
        for x in left:
            if x < minimum:
                minimum = x
        left_sorted.append(minimum)
        left.remove(minimum)

    right = A[mid:]
    right_sorted = []
    while right:
        minimum = right[0]
        for x in right:
            if x < minimum:
                minimum = x
        right_sorted.append(minimum)
        right.remove(minimum)

    merged = []
    while left_sorted and right_sorted:
        if left_sorted[0] <= right_sorted[0]:
            merged.append(left_sorted.pop(0))
        else:
            merged.append(right_sorted.pop(0))
    merged.extend(right_sorted if right_sorted else left_sorted)
    return merged
print(sortArray(A))


# 5. SORTING ITERATIVELY USING PYTHON'S BUILT IN SORTED FEATURE
def merging(A):
    mid = len(A)//2
    left = sorted(A[:mid])
    right = sorted(A[mid:])
    C = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C
print(merging(A))



# _______________________________________________________

# ADVANCED: MATRIX MULTIPLICATION


# Naive Method: Multiplying two matrices using nested loops

# 2X2 matrix "X"
X = [[1, 2],
     [2, 3]]

# 2X2 matrix "Y"
Y = [[2, 3],
     [3, 4]]

# 2X2 matrix of "0", which added to our answer, just gives us the answer
result = [[0, 0],
          [0, 0]]

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

# for end in result:
#     print(end)

# Recursive code for Matrix Multiplication

i = 0
j = 0
k = 0

def multiplyMatrixRec(row1, col1, X, row2, col2, Y, result):

    if j < col2:
        if k < col1:
            result[i][j] += X[i][k] * Y[k][j]
            k += 1
            multiplyMatrixRec(row1, col1, X, row2, col2, Y, result)
        j += 1
        multiplyMatrixRec(row1, col1, X, row2, col2, Y, result)
    i += 1
    multiplyMatrixRec(row1, col1, X, row2, col2, Y, result)


def multiplyMatrix(row1, col1, X, row2, col2, Y):
    for i in range(row1):
        for j in range(col2):
            print(result[i][j], end=" ")
        print()

row1 = 2
col1 = 2
row2 = 2
col2 = 2
multiplyMatrix(row1, col1, X, row2, col2, Y)


# _______________________________________________________

# MINDBREAKER: STRASSEN ALGORITHM

# ITERATIVE PROGRAM

import numpy as np

x = np.array([[1, 2], [2, 3]])
y = np.array([[2, 3], [3, 4]])


def strassen_iter(x, y):
    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y

    # Splitting the matrices into quadrants. See graphic
    a, b, c, d = x[0, 0], x[0, 1], x[1, 0], x[1, 1]
    e, f, g, h = y[0, 0], y[0, 1], y[1, 0], y[1, 1]

    # Computing the 7 products - this is where the magic happens!
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    # Computing the values of the 4 quadrants of the final matrix c
    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)

    return np.array([[c1, c2], [c3, c4]])

#print(strassen_iter(x, y))

# -------------------------------------------
# RECURSIVE PROGRAM

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]


def strassen_recur(x, y):
    if len(x) == 1:
        return x * y

    # Splitting the matrices into quadrants. This will be done recursively until the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen_recur(a, f - h)
    p2 = strassen_recur(a + b, h)
    p3 = strassen_recur(c + d, e)
    p4 = strassen_recur(d, g - e)
    p5 = strassen_recur(a + d, e + h)
    p6 = strassen_recur(b - d, g + h)
    p7 = strassen_recur(a - c, e + f)

    # Computing the values of the 4 quadrants of the final matrix c
    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)

    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack((c1, c2)), np.hstack((c3, c4))))

    return c

print(strassen_recur(x, y))