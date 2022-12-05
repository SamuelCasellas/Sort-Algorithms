def read_list(file_name: str) -> list:
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

def sort(array) -> list:
    for i in range(len(array)):
        for j in range(len(array)):
            if i > j:
                if array[i] < array[j]:
                    tmp = array[j]
                    array[j] = array[i]
                    array[i] = tmp


def main(): 
    array = None
    while array is None:
        array = read_list('list.txt')
    array = sort(array)
    print(*array)

if __name__ == '__main__':
    main()
