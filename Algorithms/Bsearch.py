
def binary_search(array, item):
    begin_index = 0
    end_index = len(array) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = array[midpoint]

        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

array = [1, 23, 43, 54, 62, 63, 67, 89]
item = 67


print(binary_search(array, item))