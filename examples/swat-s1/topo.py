"""
swat-s1 topology
"""

from mininet.topo import Topo

from utils import IP, MAC, NETMASK


class SwatTopo(Topo):

    """SWaT 6 plcs + attacker + private dirs."""

    def build(self):

       # self.addController('c0')

        switch = self.addSwitch('s1')
        firewall= self.addSwitch('f1')
        self.addLink(switch,firewall)

        plc1 = self.addHost(
            'plc1',
            ip=IP['plc1'] + NETMASK,
            mac=MAC['plc1'])
        self.addLink(plc1, switch)

        plc2 = self.addHost(
            'plc2',
            ip=IP['plc2'] + NETMASK,
            mac=MAC['plc2'])
        self.addLink(plc2, switch)

        plc3 = self.addHost(
            'plc3',
            ip=IP['plc3'] + NETMASK,
            mac=MAC['plc3'])
        self.addLink(plc3, switch)

        plc4 = self.addHost(
            'plc4',
            ip=IP['plc4'] + NETMASK,
            mac=MAC['plc4'])
        self.addLink(plc4, switch)

        plc5 = self.addHost(
            'plc5',
            ip=IP['plc5'] + NETMASK,
            mac=MAC['plc5'])
        self.addLink(plc5, switch)

        plc6 = self.addHost(
            'plc6',
            ip=IP['plc6'] + NETMASK,
            mac=MAC['plc6'])
        self.addLink(plc6, switch)

        extattacker= self.addHost(
            'att1',
            ip=IP['att1'] + NETMASK,
            mac=MAC['att1']
        )
        self.addLink(extattacker,firewall)

        attacker = self.addHost(
            'attacker',
            ip=IP['attacker'] + NETMASK,
            mac=MAC['attacker'])
        self.addLink(attacker, switch)
