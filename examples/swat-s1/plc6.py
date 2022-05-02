
"""
swat-s1 plc5
"""

from minicps.devices import PLC
from utils import PLC6_DATA, STATE, PLC6_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP, LS_601_M
import time
import logging



PLC6_ADDR = IP['plc6']

LS601_6 = ('LS601', 6)

P601 = ('P601',6)

class SwatPLC6(PLC):

    def pre_loop(self, sleep=0.2):
        #print 'DEBUG: swat-s1 plc6 enters pre_loop'
     
        logging.basicConfig(filename='logs/plc6log.log', encoding ='utf-8', level=logging.DEBUG, filemode = 'w', format='%(asctime)s %(levelname)-8s %(message)s')
        time.sleep(sleep)

    def main_loop(self):
        """plc6 main loop.

            - read UF tank level from the sensor
            - update internal enip server
        """

       # print 'DEBUG: swat-s1 plc6 enters main_loop.'
 

        count = 0
        while(count <= PLC_SAMPLES):
            logging.debug('plc 6 count : %d', count)
            ls601 = float(self.get(LS601_6))
           # print "DEBUG PLC6 - get lit601: %f" % ls601
            self.send(LS601_6, ls601, PLC6_ADDR)


            if ls601 <= LS_601_M['L'] :
                self.set(P601,0)
               # print "INFO PLC6 - LS601 under LS601_L or  -> close p601"
            else :
                self.set(P601,1)
               # print "INFO PLC6 - LS601 under LS601_L or  -> open p601"
         
            time.sleep(PLC_PERIOD_SEC)
            count += 1

        print 'DEBUG swat plc6 shutdown'


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc6 = SwatPLC6(
        name='plc6',
        state=STATE,
        protocol=PLC6_PROTOCOL,
        memory=PLC6_DATA,
        disk=PLC6_DATA)
