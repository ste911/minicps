"""
swat-s1 run.py
"""

from mininet.net import Mininet
from mininet.cli import CLI
from minicps.mcps import MiniCPS

from topo import SwatTopo

import sys
import time

class SwatS1CPS(MiniCPS):

    """Main container used to run the simulation."""
    def __init__(self, name, net):

        self.name = name
        self.net = net
        net.start()
        
        #net.pingAll()
       

        # start devices
        plc1, plc2, plc3, plc4, plc5, plc6, s1 = self.net.get(
            'plc1', 'plc2', 'plc3', 'plc4', 'plc5', 'plc6', 's1')

        net.startTerms()
      
        # SPHINX_SWAT_TUTORIAL RUN(
 
        net.controllers[0].cmd(sys.executable + ' swat_gui.py &')
        
        plc6.cmd(sys.executable + ' plc6.py &')
        plc5.cmd(sys.executable + ' plc5.py &')
        plc4.cmd(sys.executable + ' plc4.py &')
        plc3.cmd(sys.executable + ' plc3.py &')
        plc2.cmd(sys.executable + ' plc2.py &')
        plc1.cmd(sys.executable + ' plc1.py &')
        #time.sleep(10)
        #s1.cmd(sys.executable + ' physical_process.py &')
        s1.cmd(sys.executable + ' physical_process_rwt.py  &')
        s1.cmd(sys.executable + ' physical_process_nacl.py &')
        s1.cmd(sys.executable + ' physical_process_hcl.py &')
        s1.cmd(sys.executable + ' physical_process_naocl.py &')
        s1.cmd(sys.executable + ' physical_process_ufft.py &')
        s1.cmd(sys.executable + ' physical_process_rof.py &')
        s1.cmd(sys.executable + ' physical_process_nahso3.py &')
        s1.cmd(sys.executable + ' physical_process_rof.py &')
        s1.cmd(sys.executable + ' physical_process_rop.py &')
        # SPHINX_SWAT_TUTORIAL RUN)

        CLI(self.net)

        net.stop()

if __name__ == "__main__":

    topo = SwatTopo()
    net = Mininet(topo=topo)
    swat_s1_cps = SwatS1CPS(
        name='swat_s1',
        net=net)
