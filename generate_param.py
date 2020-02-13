import os
import yaml
import itertools
from tuneparam import TuneParam

class GenerateParam:
    """This funcion is used to generate parameters for running experiments
    """
    def __init__(self):
       print ("[STATUS]: initializing GenerateParam class")
       self.confs=self.set_design_space()
       (testnum, RA, TMR,
       gain1, gain2)=self.get_configuration()
       self.tp=TuneParam(testnum, RA, TMR,
                         gain1, gain2)
    def set_design_space(self):
        """This function is used to set the design space
        """  
        with open("config.yaml","r") as fp:
            config=yaml.load(fp)
        config=config["config"]["design_space"]
        bounds=list()
        # get configuration options values
        for _,val in config.iteritems():
            bounds.append(val)
        permutation=list(itertools.product(*bounds))
        return [list(x) for x in permutation]
    
    def get_configuration(self):
        """This function is used to get configuration
        """
        index=1
        return self.confs[index]

