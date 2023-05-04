from __future__ import print_function
from __future__ import absolute_import

import optparse, sys, os, m5
from caches import *
import constants as ct
from m5.objects import *

m5.util.addToPath("./")
m5.util.addToPath("../")

# 0 - LQ_ENTRIES = [32, 64]
# 1 - SQ_ENTRIES = [32, 64]
# 2 - L1D_SIZE = ['32kB', '64kB']
# 3 - L1I_SIZE = ['8kB', '16kB']
# 4 - L2_SIZE = ['256kB', '512kB']
# 5 - BP_TYPE = [TournamentBP, BiModeBP]
# 5 - ROB_ENTRIES = [128, 192]
# 7 - IQ_ENTRIES = [16, 64]

LQ_ENTRIES = 32
SQ_ENTRIES = 32
L1D_SIZE = "32kB"
L1I_SIZE = "8kB"
L2_SIZE = "256kB"
BP_TYPE = TournamentBP
ROB_ENTRIES = 128
IQ_ENTRIES = 16

RANKED = ["22222122", "12222122", "22122122", "12122122", "22121122", \
          "12121122", "12221122", "22221122", "21222122", "11222122"]


parser = optparse.OptionParser()
parser.add_option("-c", "--cmd", default="",
                    help="The binary to run in syscall emulation mode.")
parser.add_option("-a", "--args", default="1111111111",
                    help="Choosing the different args")
parser.add_option("-r", "--rank", type="int", default=0,
                    help = "Which of the top 10 configuration")
(options, args) = parser.parse_args()


# Handle ranking configuration
if (options.rank != 0) and (options.rank <= 10): 
    print("Running Rank {} configuration".format(options.rank))
    configuration = RANKED[options.rank - 1]
else:
    if options.rank != 0:
        print("Only top 10 configurations are supported. Running default configuration.")
    configuration = options.args


# Arguments
LQ_ENTRIES = ct.LQ_ENTRIES[int(configuration[0]) - 1]
SQ_ENTRIES = ct.SQ_ENTRIES[int(configuration[1]) - 1]
L1D_SIZE = ct.L1D_SIZE[int(configuration[2]) - 1]
L1I_SIZE = ct.L1I_SIZE[int(configuration[3]) - 1]
L2_SIZE = ct.L2_SIZE[int(configuration[4]) - 1]
BP_TYPE = ct.BP_TYPE[int(configuration[5]) - 1]
ROB_ENTRIES = ct.ROB_ENTRIES[int(configuration[6]) - 1]
IQ_ENTRIES = ct.IQ_ENTRIES[int(configuration[7]) - 1]


system = System(cpu = ct.CPU_MODEL(),
                mem_mode = ct.MEM_MODE,
                mem_ranges = [AddrRange(ct.MEM_SIZE)],
                cache_line_size = ct.CACHE_LINE)

# Create clock and voltage domains
system.voltage_domain = VoltageDomain(voltage = '1V')
system.clk_domain = SrcClockDomain(clock = ct.CLOCK_FREQ, voltage_domain = system.voltage_domain)

system.cpu.icache = L1_ICache(size = L1I_SIZE)       # Create the L1 instr cache
system.cpu.dcache = L1_DCache(size = L1D_SIZE)       # Create the L1 data cache
system.cpu.l2cache = L2Cache(size = L2_SIZE)         # Create the L2 cache

system.membus = SystemXBar()
system.system_port = system.membus.cpu_side_ports

system.l2bus = L2XBar()

system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

system.cpu.l2cache.connectCPUSideBus(system.l2bus)
system.cpu.l2cache.connectMemSideBus(system.membus)

system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

r = system.mem_ranges[0]
dram_intf = ct.MEM_TYPE()
dram_intf.range = m5.objects.AddrRange(r.start, size = r.size())

system.mem_ctrl = m5.objects.MemCtrl()
system.mem_ctrl.dram = dram_intf
system.mem_ctrl.port = system.membus.mem_side_ports

system.cpu.numRobs = ct.NUM_ROB

system.cpu.LQEntries = LQ_ENTRIES
system.cpu.SQEntries = SQ_ENTRIES
system.cpu.numROBEntries = ROB_ENTRIES
system.cpu.numIQEntries = IQ_ENTRIES

system.cpu.branchPred = BP_TYPE()

binary = options.cmd
process = Process()
process.cmd = [binary]

system.workload = SEWorkload.init_compatible(binary)
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system=False, system=system)

m5.instantiate()
print("**** REAL SIMULATION ****")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))
if exit_event.getCode() != 0:
    print("Simulated exit code not 0! Exit code is", exit_event.getCode())
