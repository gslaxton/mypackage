def top_n(items,n):
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 3]
    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: #if this item is bigger than next item..
                items[j], items [j+1] = items[j+1], items [j] # swap the two

    # get the last two items
    top_n = items[-n:]

    #return the top in descending order
    return top_n[::-1]    
