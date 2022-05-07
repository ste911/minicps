"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import  HCl_PUMP_FLOWRATE_OUT
from utils import  HCl_TANK_HEIGHT, HCl_TANK_SECTION, HCl_TANK_DIAMETER
from utils import  HCLT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES

import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(
MV201 = ('MV201', 2)

#P101 = ('P101', 1)
P203 = ('P203', 2)
LS202 = ('LS202', 2)

LIT101 = ('LIT101', 1)
LIT301 = ('LIT301', 3)
LIT401 = ('LIT401', 4)

      

class HClTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(P203, 0)
        self.level = self.set(LS202, 1)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

    def main_loop(self):

        count = 0
        while(count <= PP_SAMPLES):
            
            new_level = self.level
            p203 = self.get(P203)
            mv201 = self.get(MV201)
            hcl_volume = self.section * new_level
            logging.debug('HClTank count %d', count)
            if int(p203) == 1 and int(mv201)==1:
                outflow = HCl_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                hcl_volume -= outflow

            # compute new hcl_level
            new_level = hcl_volume / self.section
           
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('HClTank new level %f with delta %f', new_level, new_level -self.level)
            self.level =  self.set(LS202, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)


if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)
    
    hclt = HClTank(
        name='hclt',
        state=STATE,
        protocol=None,
        section=HCl_TANK_SECTION,
        level=HCLT_INIT_LEVEL
    )




    
