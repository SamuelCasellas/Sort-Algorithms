import timeit

def driver():
  while True:
    input_list = [i for i in range(int(input()), -1, -1)]
    input_list_1 = input_list#.copy()
    print(sorted(input_list_1))
    t = timeit.Timer(lambda: sort(input_list)) 
    t1 = timeit.Timer(lambda: sorted(input_list_1)) 
    print (t.timeit(5))
    print (t1.timeit(5))

def main() -> None:
  driver()
  # print('\n'*50)
  # array = None

  # while array is None:
  #   file_name = 'list.txt' # file_name = input('Enter file name: ')
  #   array = read(file_name)

  # # Base case
  # if len(array) < 2:
  #   print(*array)
  #   return 

  # array = sort(array)
  # print(*array)

def read(file_name: str) -> list[int]:
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

def sort(array: list[int]) -> list[int]:
  size = len(array)
  src = array

  # Create des array of the same length as src
  # with 0's as placeholders
  des = [0 for _ in range(size)]
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
      begin1 = end2

    # Swap des and src array 
    tmp = des
    des = src
    src = tmp

  return src

def _combine(src: list[int], des: list[int], begin1: int, 
             begin2: int, end2: int) -> list[int]:
  ''' Take two sub arrays from src array indicated with three pointers
  begin1, begin2, and end2 and integrate them into array des.
  Params: src - the source array (list[int]), 
   '''
  end1 = begin2 # O(1)

  for i in range(begin1, end2): # O(n^2)
    if begin1 < end1 and (begin2 == end2 or src[begin1] < src[begin2]): # O(n)
      des[i] = src[begin1]
      begin1 += 1 # O(1)
    else:
      des[i] = src[begin2]
      begin2 += 1 # O(1)

  return des # superfluous

if __name__ == '__main__':
	main()