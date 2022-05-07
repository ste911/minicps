"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank


from utils import  NaHSO3_PUMP_FLOWRATE_OUT
from utils import NaHSO3_TANK_HEIGHT, NaHSO3_TANK_SECTION, NaHSO3_TANK_DIAMETER
from utils import  NAHSO3T_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES


import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(
MV501 = ('MV501', 5)

P401 = ('P401', 4)
P403 = ('P403', 4)
P501 = ('P501', 5)

LS401 = ('LS401', 4)


class NaHSO3Tank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.level = self.set(LS401, 0.800)
        
        # SPHINX_SWAT_TUTORIAL STATE INIT)

    def main_loop(self):

        count = 0
        while(count <= PP_SAMPLES):
            new_level = self.level
            p403 = self.get(P403)
            p401 = self.get(P401)
            p501 = self.get(P501)
            mv501 = self.get(MV501)
            
            nahso3_volume = self.section * new_level
            logging.debug('NaHSO3Tank count %d', count)
            if int(p403) == 1 and int(p501)==1 and int(mv501)==1 :
                outflow = NaHSO3_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                nahso3_volume -= outflow

            # compute new hcl_level
            new_level = nahso3_volume / self.section
           
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('NaHSO3Tank new level %f with delta %f', new_level, new_level -self.level)
            self.level = self.set(LS401, new_level)

            if int(p401) ^ int(p403):
                self.set(P403,p401)

            count += 1
            time.sleep(PP_PERIOD_SEC)



if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    nahso3t = NaHSO3Tank(
        name='nahso3t',
        state=STATE,
        protocol=None,
        section=NaHSO3_TANK_SECTION,
        level=NAHSO3T_INIT_LEVEL
    )




    
