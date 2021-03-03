"""
util.py file is use to define helper functions
Created by: Priyank Dharani 03/01/2021
Modefied by:
"""

def check_required_args(request,*args):
    for key in args:
        print(key)
        if key not in request:
            raise KeyError('Arguments %s are required' % (', '.join(args)))