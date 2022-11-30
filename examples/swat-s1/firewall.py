from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr

rules= [['AA:AA:AA:AA:AA:BB','00:1D:9C:C7:B0:70'],
        ['AA:AA:AA:AA:AA:BB','00:1D:9C:C8:BC:46'],
        ['AA:AA:AA:AA:AA:BB','00:1D:9C:C8:BD:F2'],
        ['AA:AA:AA:AA:AA:BB','00:1D:9C:C7:FA:2C'],
        ['AA:AA:AA:AA:AA:BB','00:1D:9C:C8:BC:2F'],
        ['AA:AA:AA:AA:AA:BB','00:1D:9C:C7:FA:2D']]

class SDNFirewall (EventMixin):

    def __init__(self):
        self.listenTo(core.openflow)

    def _handle_ConnectionUp (self,event):
        for rule in rules:
            block = of.ofp_match()
            block.dl_src = EthAddr(rule[0])
            block.dl_dst = EthAddr(rule[1])
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            event.connection.send(flow_mod)
def launch():
    core.registerNew(SDNFirewall)        





