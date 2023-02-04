def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    a=0
    b=0
    for i in people:
        x=people[i]
        if x>a:
            a=x
            b=i
    return b
    
print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))
