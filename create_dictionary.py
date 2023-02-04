def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    d={}

    for i in key:
        for j in value:
            d.setdefault(i,j)
        
    return d
    
print(create_dictionary(key=[1,2,3],value= ["one", "two", "three"]))