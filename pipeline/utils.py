from functools import partial
'''Util functions
'''

def makeGen(fun):
    '''returns a generator function
    which takes an iterable `inList` and returns another generator
    formed by applying `fun` to each element of `inList`
    '''
    def foo(inList, *args, **kwargs):
        for i in inList:
            yield fun(i, *args, **kwargs)
    return foo

def fOg(f1,f2):
    return lambda x : f1(f2(x))

def _appedTofile(fun, csvFile):
    '''return decorator that will append a line to filename
    do not use this function.
    use fileDecor instead
    this method can be extended for all side-effect operations
    but aint nobody got time for that
    '''
    def ret_fun(arg):
        #type of arg should be that of dict
        ret =  fun(arg)
        print "%s.writerow(%s)" % (csvFile, arg)
        csvFile.writerow(ret)
        return ret
    return ret_fun

def fileDecor(csvFile):
    return partial(_appedTofile, csvFile=csvFile)


