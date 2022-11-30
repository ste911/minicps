"""
swat-s1 utils.py

sqlite and enip use name (string) and pid (int) has key and the state stores
values as strings.

Actuator tags are redundant, we will use only the XXX_XXX_OPEN tag ignoring
the XXX_XXX_CLOSE with the following convention:
    - 0 = error
    - 1 = off
    - 2 = on

sqlite uses float keyword and cpppo use REAL keyword.
"""

from minicps.utils import build_debug_logger

swat = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='')
# physical process {{{1
# SPHINX_SWAT_TUTORIAL PROCESS UTILS(
GRAVITATION = 9.81                # m.s^-2

# RAW WATER TANK
TANK_HEIGHT = 1.600               # m
TANK_DIAMETER = 1.38              # m
TANK_SECTION = 1.5                # m^2
PUMP_FLOWRATE_IN = 2.55           # m^3/h spec say btw 2.2 and 2.4
PUMP_FLOWRATE_OUT = 2.45          # m^3/h spec say btw 2.2 and 2.4

# HCL TANK
HCl_TANK_HEIGHT = 1.750           # m
HCl_TANK_DIAMETER = 0.55          # m
HCl_TANK_SECTION = 0.24           # m^2
HCl_PUMP_FLOWRATE_OUT = 0.00078   # m^3/h

# NACL TANK
NaCl_TANK_HEIGHT = 1.750  # m
NaCl_TANK_DIAMETER = 0.55         # m
NaCl_TANK_SECTION = 0.24          # m^2
NaCl_PUMP_FLOWRATE_OUT = 0.05     # m^3/h

# NAOCL TANK
NaOCl_TANK_HEIGHT = 1.750         # m
NaOCl_TANK_DIAMETER = 0.55        # m
NaOCl_TANK_SECTION = 0.24         # m^2
NaOCl_PUMP_FLOWRATE_OUT = 0.065   # m^3/h

# UFF TANK
UFF_TANK_HEIGHT = 1.600               # m
UFF_TANK_DIAMETER = 1.38              # m
UFF_TANK_SECTION = 1.5                # m^2
UFF_PUMP_FLOWRATE_IN = 2.55           # m^3/h spec say btw 2.2 and 2.4
UFF_PUMP_FLOWRATE_OUT = 2.45          # m^3/h spec say btw 2.2 and 2.4

# ROF TANK
ROF_TANK_HEIGHT = 1.600               # m
ROF_TANK_DIAMETER = 1.38              # m
ROF_TANK_SECTION = 1.5                # m^2
ROF_PUMP_FLOWRATE_IN = 2.55           # m^3/h spec say btw 2.2 and 2.4
ROF_PUMP_FLOWRATE_OUT = 2.45          # m^3/h spec say btw 2.2 and 2.4

# NASHO3 TANK
NaHSO3_TANK_HEIGHT = 1.750           # m
NaHSO3_TANK_DIAMETER = 0.55          # m
NaHSO3_TANK_SECTION = 0.24           # m^2
NaHSO3_PUMP_FLOWRATE_OUT = 0.00078   # m^3/h

# ROP WATER TANK
ROP_TANK_HEIGHT = 1.24                # m
ROP_TANK_DIAMETER = 1.16              # m
ROP_TANK_SECTION = 1.05               # m^2
ROP_PUMP_FLOWRATE_IN = 2.55           # m^3/h spec say btw 2.2 and 2.4
ROP_PUMP_FLOWRATE_OUT = 2.45          # m^3/h spec say btw 2.2 and 2.4




# periods in msec
# R/W = Read or Write
T_PLC_R = 100E-3
T_PLC_W = 100E-3

T_PP_R = 200E-3
T_PP_W = 200E-3
T_HMI_R = 100E-3

# ImageTk
DISPLAYED_SAMPLES = 14

# Control logic thresholds
LIT_101_MM = {  # raw water tank mm
    'LL': 250.0,
    'L': 400.0,
    'H': 800.0,
    'HH': 1200.0,
}
LIT_101_M = {  # raw water tank m
    'LL': 0.250,
    'L': 0.400,
    'H': 0.800,
    'HH': 1.200,
}

LIT_301_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 400.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LIT_301_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.400,
    'H': 1.000,
    'HH': 1.200,
}

LS_201_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 400.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LS_201_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.400,
    'H': 1.000,
    'HH': 1.200,
}
LS_202_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 400.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LS_202_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.400,
    'H': 1.000,
    'HH': 1.200,
}
LS_203_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 400.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LS_203_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.400,
    'H': 1.000,
    'HH': 1.200,
}

LIT_401_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 400.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LIT_401_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.40,
    'H': 1.000,
    'HH': 1.200,
}

LS_401_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 400.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LS_401_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.400,
    'H': 1.000,
    'HH': 1.200,
}

LS_601_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 300.0,
    'H': 1000.0,
    'HH': 1200.0,
}

LS_601_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.300,
    'H': 1.000,
    'HH': 1.200,
}

PLC_PERIOD_SEC = 0.40  # plc update rate in seconds
PLC_PERIOD_HOURS = PLC_PERIOD_SEC / 3600.0
PLC_SAMPLES = 1000

PP_RESCALING_HOURS = 100
PP_PERIOD_SEC = 0.40  # physical process update rate in seconds
PP_PERIOD_HOURS = (PP_PERIOD_SEC / 3600.0) * PP_RESCALING_HOURS
PP_SAMPLES = int(PLC_PERIOD_SEC / PP_PERIOD_SEC) * PLC_SAMPLES

#INIT LEVELS
RWT_INIT_LEVEL = 0.500      # m
HCLT_INIT_LEVEL = 0.500     # m
NACLT_INIT_LEVEL = 0.500    # m
NAOCLT_INIT_LEVEL = 0.500   # m
UFFT_INIT_LEVEL = 0.500     # m
ROFT_INIT_LEVEL = 0.500     # m
NAHSO3T_INIT_LEVEL = 0.500  # m
ROPT_INIT_LEVEL = 0.500      # m

# SPHINX_SWAT_TUTORIAL PROCESS UTILS)

# topo {{{1
IP = {
    'plc1': '192.168.1.10',
    'plc2': '192.168.1.20',
    'plc3': '192.168.1.30',
    'plc4': '192.168.1.40',
    'plc5': '192.168.1.50',
    'plc6': '192.168.1.60',
    'attacker': '192.168.1.77',
    'attacker2': "192.168.1.177",
}

NETMASK = '/24'

MAC = {
    'plc1': '00:1D:9C:C7:B0:70',
    'plc2': '00:1D:9C:C8:BC:46',
    'plc3': '00:1D:9C:C8:BD:F2',
    'plc4': '00:1D:9C:C7:FA:2C',
    'plc5': '00:1D:9C:C8:BC:2F',
    'plc6': '00:1D:9C:C7:FA:2D',
    'attacker': 'AA:AA:AA:AA:AA:AA',
    'attacker2': 'AA:AA:AA:AA:AA:BB',
}


# others
# TODO
PLC1_DATA = {
    'TODO': 'TODO',
}
# TODO
PLC2_DATA = {
    'TODO': 'TODO',
}
# TODO
PLC3_DATA = {
    'TODO': 'TODO',
}
# TODO
PLC4_DATA = {
    'TODO': 'TODO',
}
# TODO
PLC5_DATA = {
    'TODO': 'TODO',
}
# TODO
PLC6_DATA = {
    'TODO': 'TODO',
}


# SPHINX_SWAT_TUTORIAL PLC1 UTILS(
PLC1_ADDR = IP['plc1']
PLC1_TAGS = (
    ('MV101', 1, 'INT'),
    ('LIT101', 1, 'REAL'),
    ('P101', 1, 'INT'),
    # interlocks does NOT go to the statedb
    ('LS201', 1, 'REAL'),
    ('LS202', 1, 'REAL'),
    ('LS203', 1, 'REAL'),
    ('MV201', 1, 'INT'),
    ('LIT301', 1, 'REAL'),
)
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}
# SPHINX_SWAT_TUTORIAL PLC1 UTILS)

PLC2_ADDR = IP['plc2']
PLC2_TAGS = (
    ('MV201', 2, 'INT'),
    ('P201', 2, 'INT'),
    ('LS201', 2, 'REAL'),
    ('P203', 2, 'INT'),
    ('LS202', 2, 'REAL'),
    ('P205', 2, 'INT'),
    ('LS203', 2, 'REAL'),
    ('LIT301', 2 , 'REAL')
    # no interlocks
)
PLC2_SERVER = {
    'address': PLC2_ADDR,
    'tags': PLC2_TAGS
}
PLC2_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC2_SERVER
}

PLC3_ADDR = IP['plc3']
PLC3_TAGS = (
    ('LIT301', 3, 'REAL'),
    ('P301', 3, 'INT'),
    ('MV302', 3, 'INT'),

    ('LIT401', 3, 'REAL'),
    # no interlocks
)
PLC3_SERVER = {
    'address': PLC3_ADDR,
    'tags': PLC3_TAGS
}
PLC3_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC3_SERVER
}
PLC4_ADDR = IP['plc4']
PLC4_TAGS = (
    ('P401', 4, 'INT'),
    ('P403', 4, 'INT'),
    ('LIT401', 4, 'REAL'),
    ('LS401', 4 , 'REAL'),
    ('LS601', 4 , 'REAL')
)
PLC4_SERVER = {
    'address': PLC4_ADDR,
    'tags': PLC4_TAGS
}
PLC4_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC4_SERVER
}
PLC5_ADDR = IP['plc5']
PLC5_TAGS = (
    ('P501', 5, 'INT'),
    ('MV501', 5, 'INT'),
    ('LIT401', 5, 'REAL'),
    ('LS401', 5, 'REAL'),
    ('LS601', 5, 'REAL'),

)
PLC5_SERVER = {
    'address': PLC5_ADDR,
    'tags': PLC5_TAGS
}
PLC5_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC5_SERVER
}
PLC6_ADDR = IP['plc6']
PLC6_TAGS = (
    ('LS601', 6, 'REAL'),
    ('P601', 6, 'INT'),
)
PLC6_SERVER = {
    'address': PLC6_ADDR,
    'tags': PLC6_TAGS
}
PLC6_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC6_SERVER
}


# state {{{1
# SPHINX_SWAT_TUTORIAL STATE(
PATH = 'swat_s1_db.sqlite'
NAME = 'swat_s1'

STATE = {
    'name': NAME,
    'path': PATH
}
# SPHINX_SWAT_TUTORIAL STATE)

SCHEMA = """
CREATE TABLE swat_s1 (
    name              TEXT NOT NULL,
    pid               INTEGER NOT NULL,
    value             TEXT,
    PRIMARY KEY (name, pid)
);
"""

SCHEMA_INIT = """
    INSERT INTO swat_s1 VALUES ('MV101',    1, '0');
    INSERT INTO swat_s1 VALUES ('LIT101',   1, '0.500');
    INSERT INTO swat_s1 VALUES ('P101',     1, '1');

    INSERT INTO swat_s1 VALUES ('MV201',    2, '0');
    INSERT INTO swat_s1 VALUES ('P201',    2, '0');
    INSERT INTO swat_s1 VALUES ('LS201',    2, '1');
    INSERT INTO swat_s1 VALUES ('P203',    2, '0');
    INSERT INTO swat_s1 VALUES ('LS202',    2, '1');
    INSERT INTO swat_s1 VALUES ('P205',    2, '0');
    INSERT INTO swat_s1 VALUES ('LS203',    2, '1');

    INSERT INTO swat_s1 VALUES ('LIT301',   3, '0.500');
    INSERT INTO swat_s1 VALUES ('P301',    3, '0');
    INSERT INTO swat_s1 VALUES ('MV302',    3, '0');

    INSERT INTO swat_s1 VALUES ('P401',     4, '0');
    INSERT INTO swat_s1 VALUES ('P403',     4, '0');
    INSERT INTO swat_s1 VALUES ('LIT401',   4, '0.000');
    INSERT INTO swat_s1 VALUES ('LS401',    4, '1');

    INSERT INTO swat_s1 VALUES ('P501',   5, '0');
    INSERT INTO swat_s1 VALUES ('MV501',   5, '0');

    INSERT INTO swat_s1 VALUES ('P601',    6, '0');
    INSERT INTO swat_s1 VALUES ('LS601',    6, '0');
"""
