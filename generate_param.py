import os
import yaml
import itertools
import GPyOpt
import numpy as np
import pandas as pd
from tuneparam import TuneParam
from GPyOpt.methods import BayesianOptimization

class GenerateParam:
    """This funcion is used to generate parameters for running experiments
    """
    def __init__(self, mode):

       print ("[STATUS]: initializing GenerateParam class")

       self.NUM_INIT=20
       self.NUM_CONF_OPTIONS=5
       if mode == "RUN":
           # get all the configurations in the design space
           self.confs=self.set_design_space()
           # get initial configurations that will be measured
           self.init_confs=self.get_init_configs()
           # measure initial configurations
           for cur_init_conf in self.init_confs:
               testnum, RA, TMR, gain1, gain2=cur_init_conf
               with open("cur_config.yaml","w") as curfp:
                   yaml.dump(dict(cur_config=cur_init_conf),curfp,default_flow_style=False)
               print ("[STATUS]: current configuration: {0} {1} {2} {3} {4}".format(
                             testnum, RA, TMR, gain1, gain2))
               self.tp=TuneParam(np.array(cur_init_conf))
       elif mode == "BO":
           self.get_bounds()
           self.run_bo()
       else:
           print ("[ERROR]: mode not supported")
    
    def func(self, cur_config):
        """This function is used to measure next config"""
        TuneParam(cur_config)
    def get_bounds(self):
        """This function is used to get bounds"""
        self.bounds = [
                  {'name': 'testnum', 'type': 'discrete', 'domain': (10)},
                  {'name': 'RA', 'type': 'discrete', 'domain': (5e-12, 10e-12, 15e-12, 20e-12)},
                  {'name': 'TMR', 'type': 'discrete', 'domain': (100, 150, 200, 250, 300, 350, 400)},
                  {'name': 'gain1', 'type': 'discrete', 'domain': (5,6,7,8,9,10,
                                                                    11,12,13,14,15,
                                                                    16,17,18,19,20,
                                                                    21,22,23,24,25,
                                                                    26,27,28,29,30,
                                                                    31,32,33,34,35,
                                                                    36,37,38,39,40,
                                                                    41,42,43,44,45,
                                                                    46,47,48,49,50)},
                  {'name': 'gain2', 'type': 'discrete', 'domain': (5,6,7,8,9,10,
                                                                    11,12,13,14,15,
                                                                    16,17,18,19,20,
                                                                    21,22,23,24,25,
                                                                    26,27,28,29,30,
                                                                    31,32,33,34,35,
                                                                    36,37,38,39,40,
                                                                    41,42,43,44,45,
                                                                    46,47,48,49,50)}
        ]

    def run_bo(self):
        """This function is used to run bayesian optimization"""
        max_iter=50
        BO=GPyOpt.methods.BayesianOptimization(f=self.func, domain=self.bounds, initial_design_numdata=self.NUM_INIT,
                                              acquisition_type='EI', exact_feval=True)
        BO.run_optimization(max_iter)

    def set_design_space(self):
        """This function is used to set the design space
        """
        with open("config.yaml","r") as fp:
            config=yaml.load(fp)
        config=config["config"]["design_space"]
        bounds=[[] for i in range(0,self.NUM_CONF_OPTIONS)]
        # get configuration options values
        for key,val in config.iteritems():
            if key=="testnum":
                bounds[0]=val
            elif key=="RA":
                bounds[1]=val
            elif key=="TMR":
                bounds[2]=val
            elif key=="gain1":
                bounds[3]=val
            elif key=="gain2":
                bounds[4]=val
            else:
               print ("[ERROR]: configuration option not supported")
               return
        permutation=list(itertools.product(*bounds))
        return [list(x) for x in permutation]

    def get_init_configs(self):
        """This function is used to get configuration
        """
        from random import randint
        from operator import itemgetter
        index=[randint(0,len(self.confs)) for i in range(0,self.NUM_INIT)]
        return itemgetter(*index)(self.confs)
