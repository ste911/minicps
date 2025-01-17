
"""
swat-s1 plc2
""" 

from minicps.devices import PLC
from utils import PLC2_DATA, STATE, PLC2_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP
from utils import  LIT_101_M, LIT_301_M, LS_201_M,LS_202_M,LS_203_M, FIT_201_THRESH

import time
import logging

PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

FIT201_2 = ('FIT201', 2)
LS201_2 = ('LS201', 2)
LS202_2 = ('LS202', 2)
LS203_2 = ('LS203', 2)

P201 = ('P201', 2)
P203 = ('P203', 2)
P205 = ('P205', 2)
MV201 = ('MV201', 2)

LIT301_2 = ('LIT301', 2)

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
            logging.debug('plc 2 count : %d', count)
            #fit201 = float(self.get(FIT201_2))
            #print "DEBUG PLC2 - get fit201: %f" % fit201

           # self.send(FIT201_2, fit201, PLC2_ADDR)
            #logging.debug('1')
            #fit201 = self.receive(FIT201_2, PLC2_ADDR)
            # print "DEBUG PLC2 - receive fit201: ", fit201
            ls201 = float(self.get(LS201_2))
            #logging.debug('2')
            self.send(LS201_2, ls201, PLC2_ADDR)
            #logging.debug('3')
            ls202 = float(self.get(LS202_2))
            #logging.debug('4')
            self.send(LS202_2, ls202, PLC2_ADDR)
            #logging.debug('5')
            ls203 = float(self.get(LS203_2))
            #logging.debug('6')
            self.send(LS203_2, ls203, PLC2_ADDR)
            #logging.debug('7')

            lit301 = float(self.receive(LIT301_3, PLC3_ADDR))
            #print "DEBUG PLC2 - receive lit301: %f" % lit301
            #logging.debug('8')
            self.send(LIT301_2, lit301, PLC2_ADDR)

            if lit301 <= LIT_301_M['L'] and ls201 >= LS_201_M['L'] and ls202 >= LS_202_M['L'] \
                        and ls203 >= LS_203_M['L']:
                 # OPEN MV201
                 self.set(MV201, 1)
             #    logging.debug('17')
                 self.send(MV201, 1, PLC2_ADDR)
              #   logging.debug('18')
                 self.set(P201, 1)
               #  logging.debug('19')
                 self.send(P201, 1, PLC2_ADDR)
                # logging.debug('20')
                 self.set(P203, 1)
                 #logging.debug('21')
                 self.send(P203, 1, PLC2_ADDR)
                 #logging.debug('22')
                 self.set(P205, 1)
                 #logging.debug('23')
                 self.send(P205, 1, PLC2_ADDR)
                 #logging.debug('24')
                # print "INFO PLC1 - lit301 under LIT_301_M['L'] -> open p201/3/5 mv201."
            else:
            #if  lit301 >= LIT_301_M['H'] or ls201 <= LS_201_M['L'] \
             #         or ls202 <= LS_202_M['L'] or ls203 <= LS_203_M['L']:
                 # CLOSE MV201
                 self.set(MV201, 0)
                 #logging.debug('9')
                 self.send(MV201, 0, PLC2_ADDR)
                 #logging.debug('10')
                 self.set(P201, 0)
                 #logging.debug('11')
                 self.send(P201, 0, PLC2_ADDR)
                 #logging.debug('12')
                 self.set(P203, 0)
                 #logging.debug('13')
                 self.send(P203, 0, PLC2_ADDR)
                 #logging.debug('14')
                 self.set(P205, 0)
                 #logging.debug('15')
                 self.send(P205, 0, PLC2_ADDR)
                 #logging.debug('16')
              #   print "INFO PLC1 - fit201 under FIT_201_THRESH " \
               #        "or over LIT_301_M['H']: -> close mv201 p201/3/5."
            


            time.sleep(PLC_PERIOD_SEC)
            count += 1

        print 'DEBUG swat plc2 shutdown'


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc2 = SwatPLC2(
        name='plc2',
        state=STATE,
        protocol=PLC2_PROTOCOL,
        memory=PLC2_DATA,
        disk=PLC2_DATA)
