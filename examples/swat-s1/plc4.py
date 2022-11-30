
"""
swat-s1 plc4
"""

from minicps.devices import PLC
from utils import PLC4_DATA, STATE, PLC4_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP, LIT_401_M, LS_401_M, LS_601_M
import time
import logging


PLC4_ADDR = IP['plc4']
PLC6_ADDR = IP['plc6']

LIT401_4 = ('LIT401', 4)
LS401_4 = ('LS401', 4)
#LS601_4 = ('LS601', 4)

P401 = ('P401', 4)
P403 = ('P403', 4)

LS601_6 = ('LS601', 6)
class SwatPLC4(PLC):

    def pre_loop(self, sleep=0.2):
     #   print 'DEBUG: swat-s1 plc4 enters pre_loop'

        logging.basicConfig(filename='logs/plc4log.log', encoding ='utf-8', level=logging.DEBUG, filemode = 'w', format='%(asctime)s %(levelname)-8s %(message)s')
        time.sleep(sleep)

    def main_loop(self):
        """plc4 main loop.

            - read UF tank level from the sensor
            - update internal enip server
        """

      #  print 'DEBUG: swat-s1 plc4 enters main_loop.'

        count = 0
        while(count <= PLC_SAMPLES):
            logging.debug('plc 4 count : %d', count)
            lit401 = float(self.get(LIT401_4))
            self.send(LIT401_4, lit401, PLC4_ADDR)
            logging.debug("PLC4 - get lit401: %f",lit401)

            ls401 = float(self.get(LS401_4))
            self.send(LS401_4, ls401, PLC4_ADDR)
            logging.debug("PLC4 - get ls401: %f",ls401)

            ls601 = float(self.receive(LS601_6, PLC6_ADDR))
            #self.send(LS601_4, ls601, PLC4_ADDR)
            logging.debug("PLC4 - receive ls601: %f", ls601)

            if  lit401 <= LIT_401_M['L'] or ls401 <= LS_401_M['L'] or ls601 >= LS_601_M['H']:
                 # CLOSE MV201
                 self.set(P401, 0)
                 self.send(P401, 0, PLC4_ADDR)
                 self.set(P403, 0)
                 self.send(P403, 0, PLC4_ADDR)
                 logging.info("PLC4 - lit401 under LIT401_M['L'] "\
                    "or ls401 under LS401_M['L'] "\
                    "or ls601 over LS_601_M['H']:  -> close p401 and p403")
            else:
                 # OPEN MV201
                 self.set(P401, 1)
                 self.send(P401, 1, PLC4_ADDR)
                 self.set(P403, 1)
                 self.send(P403, 1, PLC4_ADDR)
                 logging.info("PLC4 - lit401 over LIT_401_M['L'] "\
                     "and LS401 over LS401_M['L'] "\
                     "and ls601 under LS_601_M['H'] -> open p401 and p403")

            

            time.sleep(PLC_PERIOD_SEC)
            count += 1

        logging.debug('Swat PLC4 shutdown')


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc4 = SwatPLC4(
        name='plc4',
        state=STATE,
        protocol=PLC4_PROTOCOL,
        memory=PLC4_DATA,
        disk=PLC4_DATA)
