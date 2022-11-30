
"""
swat-s1 plc3
"""

from minicps.devices import PLC
from utils import PLC3_DATA, STATE, PLC3_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP
from utils import LIT_301_M, LIT_401_M

import time
import logging

PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']
PLC4_ADDR = IP['plc4']

LIT301_3 = ('LIT301', 3)

#LIT401_3 = ('LIT401', 3)
P301 = ('P301', 3)
MV302 = ('MV302', 3)

LIT401_4 = ('LIT401', 4)


class SwatPLC3(PLC):

    def pre_loop(self, sleep=0.2):

        logging.basicConfig(filename='logs/plc3log.log', encoding ='utf-8', level=logging.DEBUG, filemode = 'w', format='%(asctime)s %(levelname)-8s %(message)s')
        time.sleep(sleep)

    def main_loop(self):
        """plc3 main loop.

            - read UF tank level from the sensor
            - update internal enip server
        """

#        print 'DEBUG: swat-s1 plc3 enters main_loop.'


        count = 0
        while(count <= PLC_SAMPLES):
            logging.debug('plc 3 count : %d', count)
            lit301 = float(self.get(LIT301_3))
            self.send(LIT301_3, lit301, PLC3_ADDR)
            logging.debug("PLC3 - get lit301: %f", lit301)


            lit401 = float(self.receive(LIT401_4, PLC4_ADDR))
            logging.debug("PLC3 - receive lit401: %f",lit401)


            if lit301 >= LIT_301_M['L'] and lit401 <= LIT_401_M['H']:
                 # OPEN MV201
                 self.set(P301, 1)
                 self.send(P301, 1, PLC3_ADDR)
                 self.set(MV302, 1)
                 self.send(MV302, 1, PLC3_ADDR)
                 logging.info("PLC3 - lit301 over LIT_301_M['H'] "\
                     " and lit401 under LIT_401_M['H']-> open p301 and mv302")
            else:
                 # CLOSE MV201
                 self.set(P301, 0)
                 self.send(P301, 0, PLC3_ADDR)
                 self.set(MV302, 0)
                 self.send(MV302, 0, PLC3_ADDR)
                 logging.info("PLC3 - lit301 under LIT301_M['L'] "\
                     "or lit401 over LIT_401_M['H']: -> close p301 and mv302")            
            time.sleep(PLC_PERIOD_SEC)
            count += 1

        logging.debug('Swat PLC3 shutdown')


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc3 = SwatPLC3(
        name='plc3',
        state=STATE,
        protocol=PLC3_PROTOCOL,
        memory=PLC3_DATA,
        disk=PLC3_DATA)
