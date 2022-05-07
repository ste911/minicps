"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import  NaOCl_PUMP_FLOWRATE_OUT
from utils import NaOCl_TANK_HEIGHT, NaOCl_TANK_SECTION, NaOCl_TANK_DIAMETER
from utils import  NAOCLT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES

import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(

MV201 = ('MV201', 2)
P205 = ('P205', 2)
LS203 = ('LS203', 2)


class NaOClTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(P205, 0)
        self.level = self.set(LS203, 1)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

    def main_loop(self):

        count = 0
        while(count <= PP_SAMPLES):
            
            new_level = self.level
            p205 = self.get(P205)
            mv201 = self.get(MV201)
            logging.debug('NaOClTank count %d', count)
            naocl_volume = self.section * new_level
            
            if int(p205) == 1 and int(mv201) ==1:
                outflow = NaOCl_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                naocl_volume -= outflow

            # compute new naocl_level
            new_level = naocl_volume / self.section
           
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('NaOClTank new level %f with delta %f', new_level, new_level -self.level)
            self.level = self.set(LS203, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)                           

if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    naoclt = NaOClTank(
        name='naoclt',
        state=STATE,
        protocol=None,
        section=NaOCl_TANK_SECTION,
        level=NAOCLT_INIT_LEVEL
    )




    
