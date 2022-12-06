import timeit

def gather_data():
    data = []
    while True:
        try:
            data.append(int(input("Enter a number: ")))
        except ValueError:
            break
    return data

def sort_data(data: list[int]) -> list[int]:
    if not confirm_list_of_nums(data): raise TypeError("Not all values are integers")
    # Base case:
    if len(data) < 2:
        return data
    data_dict, min_n, max_n = _gather_data_dict(data)
    return _iterate_data_dict(data_dict, min_n, max_n)
    
def _gather_data_dict(data: list[int]):
    data_dict = {}
    min_n = max_n = data[0]
    for n in data:
        if n > max_n:
            max_n = n
        if n < min_n:
            min_n = n
        if n in data_dict:
            data_dict[n] += 1
        else:
            data_dict[n] = 1
    return data_dict, min_n, max_n

def _iterate_data_dict(data_dict: dict, min: int, max: int) -> list[int]:
    list_to_return = []
    # This is O(n) because it iterates through the entire range of numbers
    for n in range(min, max + 1):
        try:
            # This is O(1) because it's a dictionary lookup
            list_to_return.extend([n] * data_dict[n])
        except KeyError:
            pass
    return list_to_return

def confirm_list_of_nums(data):
    for n in data:
        if not isinstance(n, int):
            print("Error: Not all values are integers")
            return False
    print("All values are integers")
    return True

def iterate_twice():
    for _ in range(2):
        for _ in range(100000):
            pass

if __name__ == "__main__":
    # data = gather_data()
    data = [n for n in range(100000, -1, -1)]
    # if confirm_list_of_nums(data):
    #     print(sort_data(data))
    
    print(timeit.timeit("iterate_twice()", setup="from __main__ import iterate_twice", number=1))
    print(timeit.timeit("sort_data(data)", setup="from __main__ import sort_data, data", number=1))
    print(timeit.timeit("sorted(data)", setup="from __main__ import data", number=1))
