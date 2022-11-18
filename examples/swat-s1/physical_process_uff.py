"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank


from utils import UFF_PUMP_FLOWRATE_IN, UFF_PUMP_FLOWRATE_OUT
from utils import UFF_TANK_HEIGHT, UFF_TANK_SECTION, UFF_TANK_DIAMETER
from utils import UFFT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES

import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(
MV201 = ('MV201', 2)
MV302 = ('MV302', 3)
MV501 = ('MV501', 5)

P101 = ('P101', 1)
P301 = ('P301', 3)

LIT301 = ('LIT301', 3)


class UFFWaterTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(MV201, 0)
        self.set(MV302,0)
        self.level = self.set(LIT301, 0.000)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

    def main_loop(self):

        count = 0
        while(count <= PP_SAMPLES):
            
            new_level = self.level
            
            # compute water volume
            water_volume = self.section * new_level
            # inflows volumes
            p101 = self.get(P101)
            mv201 = self.get(MV201)
            mv302 = self.get(MV302)
            mv501 = self.get(MV501)
            logging.debug('UFFTank count %d', count)
            if int(mv201) == 1 and int(p101):
                inflow = UFF_PUMP_FLOWRATE_IN * PP_PERIOD_HOURS
                water_volume += inflow

            # outflows volumes
            p301 = self.get(P301)
            if int(p301) == 1 and int(mv302):
                outflow = UFF_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                water_volume -= outflow

            # compute new water_level
            new_level = water_volume / self.section
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('UFFTank new level %f with delta %f', new_level, new_level -self.level)    
            self.level = self.set(LIT301, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)


if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    ufft  = UFFWaterTank(
        name='ufft',
        state=STATE,
        protocol=None,
        section=UFF_TANK_SECTION,
        level=UFFT_INIT_LEVEL
    )




    
