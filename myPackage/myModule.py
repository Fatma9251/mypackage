def top_n(array, n):
    """ Doc string
    desc: 
        this function sorts an array in a descending order and returns the top_n values
    Return:
        the top n values
    Args:
        array: the array to sort
        n: the number of values to return
    Ex:
        top_n([8, 3, 5, 1, 2], 3) returns: [8, 5, 3]
    """
    for i in range(n):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    top_n  = array[-n:]    
    return top_n[::-1]
