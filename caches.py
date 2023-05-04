from __future__ import print_function
from __future__ import absolute_import
from m5.objects import *
import constants as ct


class L1Cache(Cache):
    assoc = ct.L1_ASSOC
    tag_latency = ct.L1_TAG_LATENCY
    data_latency = ct.L1_DATA_LATENCY
    response_latency = ct.L1_RESPONSE_LATENCY
    mshrs = ct.L1_MSHRS
    tgts_per_mshr = ct.L1_TGSTS_PER_MSHR
    
    def __init__(self, options=None):
        super(L1Cache, self).__init__()

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

    def connectCPU(self, cpu):
        raise NotImplementedError


class L1_ICache(L1Cache):
    is_read_only = True
    writeback_clean = True
    
    def __init__(self, size, options=None):
        super(L1_ICache, self).__init__(options)
        self.size = size
        
    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port


class L1_DCache(L1Cache):
    
    def __init__(self, size, options=None):
        super(L1_DCache, self).__init__(options)
        self.size = size
        
    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port


class L2Cache(Cache):
    assoc = ct.L2_ASSOC
    tag_latency = ct.L2_TAG_LATENCY
    data_latency = ct.L2_DATA_LATENCY
    response_latency = ct.L2_RESPONSE_LATENCY
    mshrs = ct.L2_MSHRS
    tgts_per_mshr = ct.L2_TGSTS_PER_MSHR
    write_buffers = 8

    def __init__(self, size, options=None):
        super(L2Cache, self).__init__()
        self.size = size
        
    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports