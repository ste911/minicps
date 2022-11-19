
"""
swat-s1 plc2
""" 

from minicps.devices import PLC
from utils import PLC2_DATA, STATE, PLC2_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP
from utils import  LIT_101_M, LIT_301_M, LS_201_M,LS_202_M,LS_203_M

import time
import logging

PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

LS201_2 = ('LS201', 2)
LS202_2 = ('LS202', 2)
LS203_2 = ('LS203', 2)

P201 = ('P201', 2)
P203 = ('P203', 2)
P205 = ('P205', 2)
MV201 = ('MV201', 2)

#LIT301_2 = ('LIT301', 2)

LIT301_3 = ('LIT301', 3)


class SwatPLC2(PLC):

    def pre_loop(self, sleep=0.2):
 #       print 'DEBUG: swat-s1 plc2 enters pre_loop'
        logging.basicConfig(filename='logs/plc2log.log', encoding ='utf-8', level=logging.DEBUG, filemode = 'w', format='%(asctime)s %(levelname)-8s %(message)s')
        time.sleep(sleep)

    def main_loop(self):
        """plc2 main loop.

            - read flow level sensors #2
            - update interal enip server
        """

#        print 'DEBUG: swat-s1 plc2 enters main_loop.'


        count = 0
        while(count <= PLC_SAMPLES):
            logging.debug('PLC2 count : %d', count)
            
            ls201 = float(self.get(LS201_2))
            self.send(LS201_2, ls201, PLC2_ADDR)
            logging.debug('PLC2 LS201: %.5f', ls201)
            
            ls202 = float(self.get(LS202_2))
            self.send(LS202_2, ls202, PLC2_ADDR)
            logging.debug('PLC2 LS202: %.5f', ls202)

            ls203 = float(self.get(LS203_2))
            self.send(LS203_2, ls203, PLC2_ADDR)
            logging.debug('PLC2 LS203: %.5f', ls203)


            lit301 = float(self.receive(LIT301_3, PLC3_ADDR))
            logging.debug("PLC2 - receive lit301: %f", lit301)
            #self.send(LIT301_2, lit301, PLC2_ADDR)

            if lit301 <= LIT_301_M['L'] and ls201 >= LS_201_M['L'] and ls202 >= LS_202_M['L'] \
                        and ls203 >= LS_203_M['L']:
                 # OPEN MV201
                 self.set(MV201, 1)
                 self.send(MV201, 1, PLC2_ADDR)
                 self.set(P201, 1)
                 self.send(P201, 1, PLC2_ADDR)
                 self.set(P203, 1)
                 self.send(P203, 1, PLC2_ADDR)
                 self.set(P205, 1)
                 self.send(P205, 1, PLC2_ADDR)
                # print "INFO PLC1 - lit301 under LIT_301_M['L'] -> open p201/3/5 mv201."

                 logging.info("PLC2 - lit301 under LIT_301_M['L'] " \
                     " and  ls201 over LS_201_M['L'] " \
                       "and ls202 over LS_202_M['L'] " \
                       "and ls203 over LS_203_M['L'] " \
                       "and lit101 over LIT_101_M['L']: " \
                      "-> open p201/3/5 mv201.")
            else:
                 # CLOSE MV201
                 self.set(MV201, 0)
                 self.send(MV201, 0, PLC2_ADDR)
                 self.set(P201, 0)
                 self.send(P201, 0, PLC2_ADDR)
                 self.set(P203, 0)
                 self.send(P203, 0, PLC2_ADDR)
                 self.set(P205, 0)
                 self.send(P205, 0, PLC2_ADDR)

                 logging.info("PLC1 - lit301 over LIT_301_M['L']" \
                       "or ls201 under LS_201_M['L'] " \
                       "or ls202 under LS_202_M['L'] " \
                       "or ls203 under LS_203_M['L'] " \
                       "or lit101 under LIT_101_M['L']: -> close p101.")


            time.sleep(PLC_PERIOD_SEC)
            count += 1

        logging.debug('Swat PLC2 shutdown')


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc2 = SwatPLC2(
        name='plc2',
        state=STATE,
        protocol=PLC2_PROTOCOL,
        memory=PLC2_DATA,
        disk=PLC2_DATA)
