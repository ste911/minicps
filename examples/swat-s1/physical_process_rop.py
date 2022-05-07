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

from utils import  NaCl_PUMP_FLOWRATE_OUT
from utils import NaCl_TANK_HEIGHT, NaCl_TANK_SECTION, NaCl_TANK_DIAMETER
from utils import  NACLT_INIT_LEVEL

from utils import  HCl_PUMP_FLOWRATE_OUT
from utils import  HCl_TANK_HEIGHT, HCl_TANK_SECTION, HCl_TANK_DIAMETER
from utils import  HCLT_INIT_LEVEL

from utils import  NaOCl_PUMP_FLOWRATE_OUT
from utils import NaOCl_TANK_HEIGHT, NaOCl_TANK_SECTION, NaOCl_TANK_DIAMETER
from utils import  NAOCLT_INIT_LEVEL

from utils import UFF_PUMP_FLOWRATE_IN, UFF_PUMP_FLOWRATE_OUT
from utils import UFF_TANK_HEIGHT, UFF_TANK_SECTION, UFF_TANK_DIAMETER
from utils import UFFT_INIT_LEVEL

from utils import ROF_PUMP_FLOWRATE_IN, ROF_PUMP_FLOWRATE_OUT
from utils import ROF_TANK_HEIGHT, ROF_TANK_SECTION, ROF_TANK_DIAMETER
from utils import ROFT_INIT_LEVEL

from utils import  NaHSO3_PUMP_FLOWRATE_OUT
from utils import NaHSO3_TANK_HEIGHT, NaHSO3_TANK_SECTION, NaHSO3_TANK_DIAMETER
from utils import  NAHSO3T_INIT_LEVEL

from utils import ROP_PUMP_FLOWRATE_IN, ROP_PUMP_FLOWRATE_OUT
from utils import ROP_TANK_HEIGHT, ROP_TANK_SECTION, ROP_TANK_DIAMETER
from utils import ROPT_INIT_LEVEL

import sys
import time
import threading
import logging


# SPHINX_SWAT_TUTORIAL TAGS(

MV501 = ('MV501', 5)
P401 = ('P401', 4)
P501 = ('P501', 5)
P601 = ('P601', 6)


LS601 = ('LS601', 6)

class ROPWaterTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.level=self.set(LS601,0.5)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

        # test underflow

    def main_loop(self):

        count = 0
        while(count <= PP_SAMPLES):
            
            new_level = self.level
            # compute water volume
            water_volume = self.section * new_level
            # inflows volumes
            mv501 = self.get(MV501)
            p401 = self.get(P401)
            p501 = self.get(P501)
            logging.debug('ROPTank count %d', count)
            if int(mv501) == 1 and int(p401)==1 and int(mv501)==1:
                inflow = ROP_PUMP_FLOWRATE_IN * PP_PERIOD_HOURS
                water_volume += inflow
                

            # outflows volumes
            p601 = self.get(P601)
            if int(p601) == 1:
                outflow = ROP_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                water_volume -= outflow

            # compute new water_level
            new_level = water_volume / self.section
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            logging.debug('ROPTank new level %f with delta %f', new_level, new_level -self.level)
            self.level = self.set(LS601, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)

if __name__ == '__main__':

    logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    ropt  = ROPWaterTank(
        name='ropt',
        state=STATE,
        protocol=None,
        section=ROP_TANK_SECTION,
        level=ROPT_INIT_LEVEL
    )




    
