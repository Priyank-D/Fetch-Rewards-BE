

def check_required_args(request,*args):
    for key in args:
        if not request.get(key):
            raise KeyError('Arguments %s are required' % (', '.join(args)))