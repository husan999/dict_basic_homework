def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """ 
    d={}
    di=0
    a=0
    for i in list(txt):
        if i.isalpha():
            a+=1
        elif i.isdigit():
            di+=1
    d.setdefault('LETTERS',a)
    d.setdefault('DIGITS',di)
    return d
print(count_all('Hello world'))