
"""
swat-s1 plc5
"""

from minicps.devices import PLC
from utils import PLC5_DATA, STATE, PLC5_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP, LIT_401_M, LS_401_M, LS_601_M
import time
import logging


PLC4_ADDR = IP['plc4']
PLC5_ADDR = IP['plc5']
PLC6_ADDR = IP['plc6']

LIT401_4 = ('LIT401', 4)
LS401_4 = ('LS401', 4)


LIT401_5 = ('LIT401', 5)
LS401_5 = ('LS401', 5)
LS601_5 = ('LS601', 5)


LS601_6 = ('LS601', 6)

P501 = ('P501', 5)
MV501 = ('MV501', 5)
class SwatPLC5(PLC):

    def pre_loop(self, sleep=4):
       # print 'DEBUG: swat-s1 plc5 enters pre_loop'
 
        logging.basicConfig(filename='logs/plc5log.log', encoding ='utf-8', level=logging.DEBUG, filemode = 'w', format='%(asctime)s %(levelname)-8s %(message)s')
        time.sleep(sleep)

    def main_loop(self):
        """plc5 main loop.

            - read UF tank level from the sensor
            - update internal enip server
        """

       # print 'DEBUG: swat-s1 plc5 enters main_loop.'

        count = 0
        while(count <= PLC_SAMPLES):
            logging.debug('plc 5 count : %d', count)
            lit401 = float(self.receive(LIT401_4, PLC4_ADDR))
            #print "DEBUG PLC5 - receive lit401: %f" % lit401
            self.send(LIT401_5, lit401, PLC5_ADDR)

            ls401 = float(self.receive(LS401_4, PLC4_ADDR))
           # print "DEBUG PLC5 - receive ls401: %f" % ls401
            self.send(LS401_5, ls401, PLC5_ADDR)

            ls601 = float(self.receive(LS601_6, PLC6_ADDR))
           # print "DEBUG PLC5 - receive ls601: %f" % ls601
            self.send(LS601_5, ls601, PLC5_ADDR)

            if  lit401 <= LIT_401_M['L'] or ls401 <= LS_401_M['L'] or ls601 >= LS_601_M['H']:
                 # CLOSE MV201
                 self.set(P501, 0)
                 self.send(P501, 0, PLC5_ADDR)
                 self.set(MV501, 0)
                 self.send(MV501, 0, PLC5_ADDR)
                 #logging.debug('close plc5 %f <= %f, %f <= %f, %f >= %f',  lit401, LIT_401_M['L'], ls401, LS_401_M['L'], ls601, LS_601_M['H'])
                 #print "INFO PLC5 - LIT401 under LIT401_L or "\
                  #   "
            else:
            #if  lit401 >= LIT_401_M['L'] and ls401 >= LS_401_M['L'] and ls601 <= LS_601_M['H']:
                    # OPEN MV201
                self.set(P501, 1)
                self.send(P501, 1, PLC5_ADDR)
                self.set(MV501, 1)
                self.send(MV501, 1, PLC5_ADDR)
                  #  print "INFO PLC5 - lit401 over LIT_401_M['L'] and"\
                   #     "LS401 over LS401_L  -> open p501 and mv501"


            #LIT401 under LIT401_L  -> close p501 and mv501"
            
            time.sleep(PLC_PERIOD_SEC)
            count += 1

        print 'DEBUG swat plc5 shutdown'


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc5 = SwatPLC5(
        name='plc5',
        state=STATE,
        protocol=PLC5_PROTOCOL,
        memory=PLC5_DATA,
        disk=PLC5_DATA)
