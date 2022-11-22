'''
Elements of this sort:

Pile - A stack of papers

Pivot - A random paper chosen from the pile
	This is a value, not an index!

2 added piles - Make 2 new piles, one consisting of papers that are 
less than the pivot and one that consists of greater ones.
	Less goes on the left
	Right goes on the right
'''

def test_sort() -> None:
    '''Test the sort function with a collection of test cases.
    Each test case is an object with the following keys:
      test_case: the name of the test case (str),
      test_input: the array input being tested (list),
      expected: the expected output of the sort function (list)'''
    test_cases = [
      {'test_case': 'Example from rubric', 
        'test_input': [31, 72, 10, 32, 18, 95, 25, 50],
        'expected': [10, 18, 25, 31, 32, 50, 72, 95]
      },
      {'test_case': 'Empty Array', 
        'test_input': [],
        'expected': []
      },
      {'test_case': 'Single number array', 
        'test_input': [2],
        'expected': [2]
      },
      {'test_case': 'Double number array', 
        'test_input': [2,1],
        'expected': [1,2]
      },
      {'test_case': 'Double number array, repeat', 
        'test_input': [2,2],
        'expected': [2,2]
      },
      {'test_case': 'Number array, uniques', 
        'test_input': [9,-21,7,3,8,12,23,1,2,6],
        'expected': [-21,1,2,3,6,7,8,9,12,23]
      },
      {'test_case': 'Number array, repeats', 
        'test_input': [2,2,6,3,4,4],
        'expected': [2,2,3,4,4,6]
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
                 expected: list) -> None:
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
    try:
        assert output == expected
    except AssertionError:
        print(test_input, 'failed!', '🚫')
    else:
        print(test_input, 'passed!', '✅')
    print('='*50)

def main() -> None:
    test_sort()
    # array = None
    # while array is None:
    #     file_name = input('\nName of file: ')
    #     array = read_file(file_name)

    # sort(array)
    # print_array(array)

def read_file(file_name: str) -> list:
    ''' Read array from selected file.
    Params - file_name: the name of the file provided by user (str)
    Returns - array: the list read from the file.'''
    try:
        with open(file_name, mode='r') as read_file:
            return_list = read_file.readlines()
            try:
                return [int(l.strip()) for l in return_list if l != '\n']
            except TypeError:
                print('Assuming list consists completely of non-integers.')
                return [l.strip() for l in return_list if l != '\n']
    except FileNotFoundError:
        print('File not found.')
        return None

def sort(array: list) -> list:
    '''
    '''
    i_start = 0
    i_end = len(array) - 1

    _sort_recursive(array, i_start, i_end)

    return array

def _sort_recursive(array: list, i_start: int, i_end: int) -> None:
    '''
    '''

    # Base case: 
    if i_start >= i_end:
        return

    i_pivot = (i_end - i_start) // 2 + i_start
    pivot = array[i_pivot]

    i_up = i_start
    i_down = i_end
    i_up_stopped = False

    while i_up < i_down:
        if array[i_up] < pivot and i_up != i_pivot:
            i_up += 1
        else:
            i_up_stopped = True

        if array[i_down] >= pivot and i_down != i_pivot:
            i_down -= 1
        elif i_up_stopped:
            i_up_stopped = False
            
            # Swap
            array[i_up], array[i_down] = array[i_down], array[i_up]

            # Update pivot if moved
            if i_pivot == i_up:
                pivot = array[i_down]
                i_pivot = i_down
            elif i_pivot == i_down:
                pivot = array[i_up]
                i_pivot = i_up

    _sort_recursive(array, i_start, i_pivot-1)
    _sort_recursive(array, i_pivot+1, i_end)

def print_array(array: list) -> None:
    print(*array)

if __name__ == '__main__':
	  main()
