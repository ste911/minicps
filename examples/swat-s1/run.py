"""
swat-s1 run.py
"""

from mininet.net import Mininet
from mininet.node import RemoteController

from mininet.cli import CLI
from minicps.mcps import MiniCPS

from topo import SwatTopo

import sys
import time
import shlex
import subprocess
import os
import signal

class SwatCLI(CLI):
    def do_exit( self, _line ):
        "Exit"
        assert self  # satisfy pylint and allow override
        return 'exited by user command'

class SwatS1CPS(MiniCPS):

    """Main container used to run the simulation."""
    def __init__(self, name, net):

        self.name = name
        self.net = net
        
        
        #net.pingAll()
       

        # start devices
        plc1, plc2, plc3, plc4, plc5, plc6, s1, f1, attacker2, attacker= self.net.get(
            'plc1', 'plc2', 'plc3', 'plc4', 'plc5', 'plc6', 's1','f1', 'attacker2','attacker')

        
      
        # SPHINX_SWAT_TUTORIAL RUN(
        
        #net.controllers[0].cmd('../../../pox/pox.py log.level --debug openflow.of_01 forwarding.l2_learning misc.firewall &')
        net.start()
        
        #net.startTerms()
        
        pids=[]
        pids.append(os.getpgid(plc6.pid))
        pids.append(os.getpgid(plc5.pid))
        pids.append(os.getpgid(plc4.pid))
        pids.append(os.getpgid(plc3.pid))
        pids.append(os.getpgid(plc2.pid))
        pids.append(os.getpgid(plc1.pid))

        net.controllers[0].cmd(sys.executable + ' swat_gui.py &')
        
        plc6.cmd(sys.executable + ' plc6.py &')
        plc5.cmd(sys.executable + ' plc5.py &')
        plc4.cmd(sys.executable + ' plc4.py &')
        plc3.cmd(sys.executable + ' plc3.py &')
        plc2.cmd(sys.executable + ' plc2.py &')
        plc1.cmd(sys.executable + ' plc1.py &')

        #uncomment this line to have physical processes running in threads insted of processes
        #s1.cmd(sys.executable + ' physical_process.py &')

        #comment these line to have physical processes running in threads insted of processes
        s1.cmd(sys.executable + ' physical_process_rwt.py  &')
        s1.cmd(sys.executable + ' physical_process_nacl.py  &')
        s1.cmd(sys.executable + ' physical_process_hcl.py  &')
        s1.cmd(sys.executable + ' physical_process_naocl.py  &')
        s1.cmd(sys.executable + ' physical_process_uff.py  &')
        s1.cmd(sys.executable + ' physical_process_rof.py  &')
        s1.cmd(sys.executable + ' physical_process_nahso3.py  &')
        s1.cmd(sys.executable + ' physical_process_rop.py  &')
            
        
        # SPHINX_SWAT_TUTORIAL RUN)
        SwatCLI(self.net)
        for pid in pids:
            if(pid != ""):
                os.killpg(pid,signal.SIGTERM)

        net.stop()
        
       

if __name__ == "__main__":
    cmd = shlex.split(
            "sudo nohup ../../../pox/pox.py \
            log.level --debug\
             openflow.of_01 forwarding.l2_learning \
             misc.firewall "
        )

    controller0 = subprocess.Popen(cmd, shell=False)
    time.sleep(0.5)
    print("pox controller: ", controller0.pid)
    topo = SwatTopo()
    net = Mininet(topo=topo, controller=RemoteController)
    swat_s1_cps = SwatS1CPS(
        name='swat_s1',
        net=net)
    
    if(controller0 != ""):
                pg = os.getpgid(controller0.pid)
                print("crtl",pg)
                os.killpg(pg,15)
    
