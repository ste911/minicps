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
MV101 = ('MV101', 1)
MV201 = ('MV201', 2)
MV302 = ('MV302', 3)
MV501 = ('MV501', 5)

P101 = ('P101', 1)
P201 = ('P201', 2)
P203 = ('P203', 2)
P205 = ('P205', 2)
P301 = ('P301', 3)
P401 = ('P401', 4)
P403 = ('P403', 4)
P501 = ('P501', 5)
P601 = ('P601', 6)

LS201 = ('LS201', 2)
LS202 = ('LS202', 2)
LS203 = ('LS203', 2)
LS401 = ('LS401', 4)
LS601 = ('LS601', 6)

LIT101 = ('LIT101', 1)
LIT301 = ('LIT301', 3)
LIT401 = ('LIT401', 4)

FIT101 = ('FIT101', 1)
FIT201 = ('FIT201', 2)
FIT301 = ('FIT301', 3)
FIT401 = ('FIT401', 4)
FIT501 = ('FIT501', 5)
FIT502 = ('FIT502', 5)


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
            #print(" count %d", count)
            #logging.debug('\t\t naocl count %d', count)
            naocl_volume = self.section * new_level
            
            if int(p205) == 1 and int(mv201) ==1:
                outflow = NaOCl_PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                #print ' outflow = PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS %f = %f * %f' %(outflow, PUMP_FLOWRATE_OUT ,PP_PERIOD_HOURS)
                # print "DEBUG RawWaterTank outflow: ", outflow
                naocl_volume -= outflow

            # compute new naocl_level
            new_level = naocl_volume / self.section
           
            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            #logging.debug('\t\t\tNaOClTank new level %f with delta %f', new_level, new_level -self.level)
            self.level = self.set(LS203, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)                           

if __name__ == '__main__':

    #logging.basicConfig(filename='logs/physicalProc.log', encoding ='utf-8', level=logging.DEBUG)


    naoclt = NaOClTank(
        name='naoclt',
        state=STATE,
        protocol=None,
        section=NaOCl_TANK_SECTION,
        level=NAOCLT_INIT_LEVEL
    )




    
