"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import ROF_PUMP_FLOWRATE_IN, ROF_PUMP_FLOWRATE_OUT
from utils import ROF_TANK_HEIGHT, ROF_TANK_SECTION, ROF_TANK_DIAMETER
from utils import ROFT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES

import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(

MV302 = ('MV302', 3)
MV501 = ('MV501', 5)


P301 = ('P301', 3)
P401 = ('P401', 4)
P501 = ('P501', 5)

LIT401 = ('LIT401', 4)
FIT301 = ('FIT301', 3)
FIT401 = ('FIT401', 4)
FIT501 = ('FIT501', 5)
FIT502 = ('FIT502', 5)


class ROFWaterTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        # SPHINX_SWAT_TUTORIAL STATE INIT)

        # test underflow
         self.level = self.set(LIT401, 0.9)
         self.set(P301, 0)
         self.set(MV302,0)

    def main_loop(self):

        count = 0
        while(count <= PP_SAMPLES):
            
            new_level = self.level
            # compute water volume
            water_volume = self.section * new_level
            # inflows volumes
            mv302 = self.get(MV302)
            p301 = self.get(P301)
            mv501 = self.get(MV501)
            logging.debug('ROFTank count %d', count)
            if int(mv302) == 1 and int(p301) == 1 :
                inflow = ROF_PUMP_FLOWRATE_IN * PP_PERIOD_HOURS
                water_volume += inflow
            else:
                self.set(FIT301, 0.00)

            # outflows volumes
            p401 = self.get(P401)
            p501 = self.get(P501)
            mv501 = self.get(MV501)
            if int(p401) == 1 and int(p501)==1 and int(mv501)==1:
                self.set(FIT401, ROF_PUMP_FLOWRATE_OUT)
                self.set(FIT501, ROF_PUMP_FLOWRATE_OUT)
                self.set(FIT502, ROF_PUMP_FLOWRATE_OUT)
                outflow = ROF_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                water_volume -= outflow
            else:
                self.set(FIT401, 0.00)
                self.set(FIT501, 0.00)
                self.set(FIT502, 0.00)

            # compute new water_level
            new_level = water_volume / self.section
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('ROFTank new level %f with delta %f', new_level, new_level -self.level)
            self.level = self.set(LIT401, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)


if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    roft  = ROFWaterTank(
        name='roft',
        state=STATE,
        protocol=None,
        section=ROF_TANK_SECTION,
        level=ROFT_INIT_LEVEL
    )




    
