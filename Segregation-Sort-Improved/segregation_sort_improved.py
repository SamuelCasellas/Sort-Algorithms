import timeit

def sort(array):
    # Base case
    if len(array) < 2:
      return array

    # Recursive case
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return sort(less) + [pivot] + sort(greater)

array = [10, 5, 2, 3]
print(sort(array))

print(timeit.timeit("sort(array)", setup="from __main__ import sort, array", number=1000))