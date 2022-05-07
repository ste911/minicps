"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank



from utils import  NaCl_PUMP_FLOWRATE_OUT
from utils import NaCl_TANK_HEIGHT, NaCl_TANK_SECTION, NaCl_TANK_DIAMETER
from utils import  NACLT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES

import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(
MV201 = ('MV201', 2)
P201 = ('P201', 2)
LS201 = ('LS201', 2)


class NaClTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(P201, 0)
        self.level = self.set(LS201, 1)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

    def main_loop(self):
        count = 0
        while(count <= PP_SAMPLES):
            
            new_level = self.level
            p201 = self.get(P201)
            mv201 = self.get(MV201)
            nacl_volume = self.section * new_level
            logging.debug('NaClTank count %d', count)
            if int(p201) == 1 and int(mv201) == 1:
                outflow = NaCl_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                nacl_volume -= outflow

            # compute new nacl_level
            new_level = nacl_volume / self.section
           
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('NaClTank new level %f with delta %f', new_level, new_level -self.level)
            self.level = self.set(LS201, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)           


if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    naclt = NaClTank(
        name='naclt',
        state=STATE,
        protocol=None,
        section=NaCl_TANK_SECTION,
        level=NACLT_INIT_LEVEL
    )




    
