from utils import fOg, makeGen

class Pipeline(object):
    def __init__(self, name, listOfPhases=[]):
        '''creates a pipeline of f(g(h(x)))
        '''
        self.name = name
        if not listOfPhases:
            self._phaseList = [emptyPhase]
        else:
            self._phaseList = list(listOfPhases)

    def add_phase(self, phase):
        self._phaseList.append(phase)

    def __str__(self):
        return "Pieline %s" % self.name

    def __repr__(self):
        phases = len(self._phaseList)
        names = [p.name for p in self._phaseList][:5]
        if phases > 5:
            names.append('...')
        return self.name + ' ' + str(names)

    def run(self, inputList):
        '''take the input (list)
        return an output list by applying each fun in self._funlist
        in reverse order'''
        combined_fun = reduce(fOg, [p.run for p in self._phaseList])
        return combined_fun(inputList)



class Phase(object):
    ''' class for a phase in the pipeline
    '''
    def __init__(self, run_fun, name=None, initial_cfg=None):
        ''' `run_fun` is a function that accepts a generator/list as first argument
        and returns a generator/list
        '''
        if name:
            self.name = name
        else:
            self.name = run_fun.__name__

        self._cfg = initial_cfg if initial_cfg else {}
        self._fun = run_fun

    def run(self, input_list):
        '''runs self._fun on the input list
        return an iterable (generator/list) as output
        '''
        return self._fun(input_list, **self.initial_cfg)

emptyPhase = Phase(lambda x : x, name="EmptyPhase")

class RowPhase(Phase):
    def __init__(self, run_fun, *args, **kwargs):
        '''like Phase, but the run_fun is expected to accept an object in the list
        and return an object'''
        fun = makeGen(run_fun)
        super(RowPhase, self).__init__(run_fun=fun, *args, **kwargs)

