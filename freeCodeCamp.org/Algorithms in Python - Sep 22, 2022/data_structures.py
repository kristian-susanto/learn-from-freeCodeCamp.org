# For the basic section, we covered- Linear Arrays:
# Linear Search
# Binary Search
# Bubble Sort
# Insertion Sort

# Advanced- Linked Lists:
# Traverse
# Search
# Insert
# Delete


# Mindbreaker- Hash Tables:
# Associative arrays
# Hash functions
# Keys-value pairs
# Collision, and
# Chaining

# _____________________________________________________________EXAMPLES____________________________________________________


# BASIC - SEARCH & SORT:

# LINEAR SEARCH

def search(arr, target):
    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 16
result = search(arr, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



# ITERATIVE BINARY SEARCH

def binary_itr(arr, start, end, target):
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return mid

    return start
    #return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 25

result = binary_itr(arr, 0, len(arr) - 1, target)
#print(result)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")


# RECURSIVE BINARY SEARCH

def binary_recur(arr, start, end, target):
    if end >= start:

        mid = start + end - 1 // 2

        if arr[mid] < target:
            binary_recur(arr, mid + 1, end, target)

        elif arr[mid] > target:
            return binary_recur(arr, start, mid - 1, target)
        else:
            return mid
    else:
        return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 10
result = binary_recur(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    


# BUBBLE SORT - OPTIMIZED


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iterations
print(bubble_optimized(A))


# BUBBLE SORT - UNOPTIMIZED

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_sort_un_op(A):
    iterations = 0

    for i in A:
        for j in range(len(A)-1):
            iterations += 1
            if A[j] > A[j+1]:
                swap(A, j, j + 1)
    return A, iterations

print(bubble_sort_un_op(A))


# INSERTION SORT - SHIFTING ELEMENTS

def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

A = [5, 2, 4, 6, 1, 3]
print(insert_sort(A))



# INSERTION SORT - SWAPPING ELEMENTS

def swap(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
    return A
print(swap(A))

# __________________________________________________________


# ADVANCED- LINKED LISTS:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.insert_new_header("Dave")

#family.delete_tail()

# print(family.search("Bob"))
family.delete_node("Amy")
family.traversal()

# _________________________________________________________


# MINDBREAKER- HASH TABLES

# NO CODE WAS DISCUSSED FOR HASH TABLES