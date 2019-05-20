import timeit
def timefunc(stmt,printr=0,returnr=0,setup=None,number=1,globals=None):
    """[Print/return time taken in seconds for a function to complete.
    Default settings - Print time taken+ return the function result]
    
    Arguments:
        stmt {str} -- [Copy and paste your function here as a string. E.g. stmt = 'multiply(5,6)']
    
    Keyword Arguments:
        printr {int} -- [0 - Print Time Taken with Function Name only
                         1 - Print Time Taken with Function Name and Arguments
                         2 - Print Nothing] (default: {0})
        returnr {int} -- [0 - Return the result of the function, e.g. multiply(5,6) = 30, returnr=0 returns 30
                          1 - Return the time taken for the function to complete
                          2 - Return both result and function] (default: {0})
        setup {str} -- [See Timeit Module] (default: {None})
        number {int} -- [See Timeit Module] (default: {1})
        globals {dict} -- [See Timeit Module] (default: {None})
    """

    template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        ret = {stmt}
    _t1 = _timer()
    return _t1 - _t0, ret
"""
    timeit.template = template
    try:
        stmt.split("(")[1]
    except:
        print("No Code Given/Code Given is not a singular function")
    funcname = stmt.split("(")[0]
    if setup == None:
        timetaken = timeit.timeit(stmt=stmt, setup=f"from __main__ import {funcname}",number=number,globals=globals)
    else:
        timetaken = timeit.timeit(stmt=stmt, setup=setup,number=number,globals=globals)

    if printr==0:
        print(f"Time Taken for {funcname}:",timetaken[0],f". Repeated {number} time(s).")
    elif printr==1:
        print(f"Time Taken for {stmt}:",timetaken[0],f". Repeated {number} time(s).")
    if returnr==0:  
        return timetaken[1]  
    elif returnr==1:
        return timetaken[0]
    elif returnr==2:
        return timetaken
