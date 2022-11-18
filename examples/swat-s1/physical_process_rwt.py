"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import PUMP_FLOWRATE_IN, PUMP_FLOWRATE_OUT
from utils import TANK_HEIGHT, TANK_SECTION, TANK_DIAMETER
from utils import LIT_101_M, RWT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES


import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(
MV101 = ('MV101', 1)
MV201 = ('MV201', 2)

P101 = ('P101', 1)


LIT101 = ('LIT101', 1)
# SPHINX_SWAT_TUTORIAL TAGS)


# TODO: implement orefice drain with Bernoulli/Torricelli formula
class RawWaterTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(MV101, 1)
        self.set(P101, 1)
        self.level = self.set(LIT101, 0.300)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

        # test underflow
         #self.set(MV101, 0)
         #self.set(P101, 1)
         #self.level = self.set(LIT101, 0.500)

    def main_loop(self):

        count = 0
        while(count <= PP_SAMPLES):
            
            new_level = self.level
            # compute water volume
            water_volume = self.section * new_level
            # inflows volumes
            mv101 = self.get(MV101)
            logging.debug('RawWaterTank count %d', count)
            if int(mv101) == 1:
                inflow = PUMP_FLOWRATE_IN * PP_PERIOD_HOURS
                water_volume += inflow
            # outflows volumes
            p101 = self.get(P101)
            mv201 = self.get(MV201)

            if int(p101) == 1 and int(mv201) == 1:
                outflow = PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                water_volume -= outflow

            # compute new water_level
            new_level = water_volume / self.section
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('RawWaterTank new level %f with delta %f', new_level, new_level -self.level)   
            
            self.level = self.set(LIT101, new_level)


            count += 1
            time.sleep(PP_PERIOD_SEC)


if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    rwt  = RawWaterTank(
        name='rwt',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=RWT_INIT_LEVEL
    )




    
