
def test_sort() -> None:
    '''Test the sort function with a collection of test cases.
    Each test case is an object with the following keys:
      test_case: the name of the test case (str),
      test_input: the array input being tested (list),
      expected: the expected output of the sort function (list)'''
    test_cases = [
      {'test_case': 'Empty Array', 
        'test_input': [],
        'expected': []
      },
      {'test_case': 'Single number array', 
        'test_input': [2],
        'expected': [2]
      },
      {'test_case': 'Number array, uniques', 
        'test_input': [9,-21,7,3,8,12,23,1,2,6],
        'expected': [-21,1,2,3,6,7,8,9,12,23]
      },
      {'test_case': 'Number array, repeats', 
        'test_input': [2,2,6,3,4,4],
        'expected': [2,2,3,4,4,6]
      },
      {'test_case': 'Already sorted', 
        'test_input': [n for n in range(10)],
        'expected': [n for n in range(10)]
      },
      {'test_case': 'Char array, uniques', 
        'test_input': ['g','d','s', 'a', 'z'],
        'expected': ['a','d','g','s','z']
      },
      {'test_case': 'Char array, repeats', 
        'test_input': ['f','f','a','b','a','s'],
        'expected': ['a','a','b','f','f','s']
      },
      {'test_case': 'String array', 
        'test_input': ['Samantha','Sam','Jeff','Alex'],
        'expected': ['Alex','Jeff','Sam','Samantha']
      },
      {'test_case': 'Large array (odd)', 
        'test_input': [n for n in range(99,0,-1)],
        'expected': [n for n in range(1,100)]
      },
      {'test_case': 'Large array (even)', 
        'test_input': [n for n in range(100,0,-1)],
        'expected': [n for n in range(1,101)]
      }
    ]

    for t in test_cases:
        _single_test(t['test_case'], t['test_input'], t['expected'])

def _single_test(test_case: str, test_input: list, 
                 expected: list) -> AssertionError:
    '''Helper function for testing out a single test case
    Generates an output and compares it to the expected result.
    Params - test_case: The name of the test (str),
      test_input: the input to be tested (list),
      expected: the expected result (list)'''
    print(f'Test Case: {test_case}\n')
    print(f'Input: {test_input}\n')
    print(f'Expected: {expected}\n')
    output = sort(test_input)
    print(f'Output: {output}\n')
    print('='*50)
    assert output == expected

def main() -> None:
    print("\n"*50)
    test_sort()
    
    # Read array from file
    # source = None

    # while source is None:
    #     file_name = input("Enter file name: ")
    #     source = read(file_name)

    # # Base case
    # if len(source) < 2:
    #     print(*source)
    #     return

    # print(sort(source))
    
def read(file_name: str) -> list:
    ''' Read array from selected file.
    Params - file_name: the name of the file provided by user (str)
    Returns - array: the list read from the file.'''
    try:
        with open(file_name, mode='r') as read_file:
            return_list = read_file.readlines()
            return [l.strip() for l in return_list if l != '\n']
    except FileNotFoundError:
        print('File not found.')
        return None

def sort(array: list) -> list:
    '''Takes an array and returns a sorted version of it.
    Algorithm efficiency: O(n log n)
    Params - array: the input array (list)
    Returns - src: the sorted array (list)'''
    size = len(array)
    src = array

    # Create des array of the same length 
    # as src with 0's as placeholders
    des = [0] * size

    # If the number of sub arrays are more than two, 
    # the array has not been sorted yet.
    num = 2
    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 += 1

            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and src[end2 - 1] <= src[end2]:
                end2 += 1

            num += 1
            _combine(src, des, begin1, begin2, end2)

            # Continue where we last left 
            # off for next iteration
            begin1 = end2

        # Swap des and src array 
        des, src = src, des

    return src

def _combine(src: list, des: list, begin1: int, 
             begin2: int, end2: int) -> None:
    '''Take two sub arrays from src array indicated with three pointers
    begin1, begin2, and end2 and integrate them into array des.
    Params: src - the source array (list), 
      des - the destination array (list),
      begin1 - The beginning of the 1st sub array (int),
      begin2 - The beginning of the 2nd sub array (int),
      end2 - The end of the 2nd sub array (int)'''

    end1 = begin2

    for i in range(begin1, end2):
        if begin1 < end1 and (begin2 == end2 or src[begin1] < src[begin2]):
            des[i] = src[begin1]
            begin1 += 1
        else:
            des[i] = src[begin2]
            begin2 += 1

if __name__ == '__main__':
	  main()