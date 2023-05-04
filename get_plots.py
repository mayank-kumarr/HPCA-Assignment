from pathlib import Path
import matplotlib.pyplot as plt

def get_all(filepath_to_stats):
    all = {}
    with open(filepath_to_stats, 'r') as f:
        for i, line in enumerate(f):
            data = line.split()
            if len(data) < 2:
                continue
            all[data[0]] = data[1]
    return all

def get_cpi(all):
    return float(all["system.cpu.cpi"])

def get_mispred_branch_count(all):
    return int(all["system.cpu.iew.branchMispredicts"])

def get_pred_nt_inc_count(all):
    return int(all["system.cpu.iew.predictedNotTakenIncorrect"])

def get_pred_t_inc_count(all):
    return int(all["system.cpu.iew.predictedTakenIncorrect"])

def get_ipc(all):
    return float(all["system.cpu.ipc"])

def get_btb_hit_percentage(all):
    return round(float(all["system.cpu.branchPred.BTBHitRatio"])*100, 4)

def get_overall_miss_cycles_dcache(all):
    return int(all["system.cpu.dcache.overallMissLatency::total"])

def get_overall_miss_rate_dcache(all):
    return float(all["system.cpu.dcache.overallMissRate::total"])

def get_avg_overall_miss_latency_dcache(all):
    return float(all["system.cpu.dcache.overallAvgMissLatency::total"])

def get_overall_miss_cycles_icache(all):
    return int(all["system.cpu.icache.overallMissLatency::total"])

def get_overall_miss_rate_icache(all):
    return float(all["system.cpu.icache.overallMissRate::total"])

def get_avg_overall_miss_latency_icache(all):
    return float(all["system.cpu.icache.overallAvgMissLatency::total"])

def get_overall_miss_cycles_l2cache(all):
    return int(all["system.cpu.l2cache.overallMissLatency::total"])

def get_overall_miss_rate_l2cache(all):
    return float(all["system.cpu.l2cache.overallMissRate::total"])

def get_avg_overall_miss_latency_l2cache(all):
    return float(all["system.cpu.l2cache.overallAvgMissLatency::total"])

def get_rob_reads(all):
    return int(all["system.cpu.rob.reads"])

def get_rob_writes(all):
    return int(all["system.cpu.rob.writes"])

def get_lsq_full_count(all):
    return int(all["system.cpu.iew.lsqFullEvents"])

def get_forw_loads_count(all):
    return int(all["system.cpu.lsq0.forwLoads"])

def get_blocked_cache_count(all):
    return int(all["system.cpu.lsq0.blockedByCache"])

ranked_stats_root = Path("m5out")
ranked_stats = [x for x in ranked_stats_root.iterdir()]
ranked_stats = sorted(ranked_stats)

cpi = []
mispred_branch_count = []
pred_nt_inc_count = []
pred_t_inc_count = []
ipc = []
btb_hit_percentage = []
overall_miss_cycles_dcache = []
overall_miss_rate_dcache = []
avg_overall_miss_latency_dcache = []
overall_miss_cycles_icache = []
overall_miss_rate_icache = []
avg_overall_miss_latency_icache = []
overall_miss_cycles_l2cache = []
overall_miss_rate_l2cache = []
avg_overall_miss_latency_l2cache = []
rob_reads = []
rob_writes = []
lsq_full_count = []
forw_loads_count = []
blocked_cache_count = []

for r in ranked_stats:
    print(f'Getting data for {r}...', end=' ')
    i = get_all(r)
    cpi.append(get_cpi(i))
    mispred_branch_count.append(get_mispred_branch_count(i))
    pred_nt_inc_count.append(get_pred_nt_inc_count(i))
    pred_t_inc_count.append(get_pred_t_inc_count(i))
    ipc.append(get_ipc(i))
    btb_hit_percentage.append(get_btb_hit_percentage(i))
    overall_miss_cycles_dcache.append(get_overall_miss_cycles_dcache(i))
    overall_miss_rate_dcache.append(get_overall_miss_rate_dcache(i))
    avg_overall_miss_latency_dcache.append(get_avg_overall_miss_latency_dcache(i))
    overall_miss_cycles_icache.append(get_overall_miss_cycles_icache(i))
    overall_miss_rate_icache.append(get_overall_miss_rate_icache(i))
    avg_overall_miss_latency_icache.append(get_avg_overall_miss_latency_icache(i))
    overall_miss_cycles_l2cache.append(get_overall_miss_cycles_l2cache(i))
    overall_miss_rate_l2cache.append(get_overall_miss_rate_l2cache(i))
    avg_overall_miss_latency_l2cache.append(get_avg_overall_miss_latency_l2cache(i))
    rob_reads.append(get_rob_reads(i))
    rob_writes.append(get_rob_writes(i))
    lsq_full_count.append(get_lsq_full_count(i))
    forw_loads_count.append(get_forw_loads_count(i))
    blocked_cache_count.append(get_blocked_cache_count(i))
    print('Done')

def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], '  '+str(y[i]), fontsize='medium', fontweight='light', horizontalalignment='center', rotation=90)

ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

plt.figure(figsize=(10,6))
plt.bar(ranks, cpi)
addlabels(ranks, cpi)
plt.xlabel("Rank")
plt.ylabel("Cycles Per Instruction (CPI)")
plt.ylim(0.722000, 0.723350)
plt.savefig("plots/01-cpi.jpg")
print("01-cpi.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, mispred_branch_count)
addlabels(ranks, mispred_branch_count)
plt.xlabel("Rank")
plt.ylabel("Mispredicted branches detected during execution")
plt.ylim(28200, 28425)
plt.savefig("plots/02-mispred_branch_count.jpg")
print("02-mispred_branch_count.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, pred_nt_inc_count)
addlabels(ranks, pred_nt_inc_count)
plt.xlabel("Rank")
plt.ylabel("Number of branches that were predicted not taken incorrectly")
plt.ylim(19800, 20000)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/03-pred_nt_inc_count.jpg")
print("03-pred_nt_inc_count.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, pred_t_inc_count)
addlabels(ranks, pred_t_inc_count)
plt.xlabel("Rank")
plt.ylabel("Number of branches that were predicted taken incorrectly")
plt.ylim(8410, 8416)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/04-pred_t_inc_count.jpg")
print("04-pred_t_inc_count.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, ipc)
addlabels(ranks, ipc)
plt.xlabel("Rank")
plt.ylabel("Instructions Per Cycle (IPC)")
plt.ylim(1.382000, 1.385000)
plt.savefig("plots/05-ipc.jpg")
print("05-ipc.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, btb_hit_percentage)
addlabels(ranks, btb_hit_percentage)
plt.xlabel("Rank")
plt.ylabel("Number of BTB Hit Percentage")
plt.ylim(99.1700, 99.2075)
plt.savefig("plots/06-btb_hit_percentage.jpg")
print("06-btb_hit_percentage.jpg saved")
plt.clf()

plt.figure(figsize=(15,18))
plt.bar(ranks, overall_miss_cycles_dcache)
addlabels(ranks, overall_miss_cycles_dcache)
plt.xlabel("Rank")
plt.ylabel("Overall Miss Cycles (DCache)")
plt.ylim(785000000, 810625000)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/07-i-overall_miss_cycles_dcache.jpg")
print("07-i-overall_miss_cycles_dcache.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, overall_miss_rate_dcache)
addlabels(ranks, overall_miss_rate_dcache)
plt.xlabel("Rank")
plt.ylabel("Overall Miss Rate (DCache)")
plt.ylim(0.006600, 0.007225)
plt.savefig("plots/07-ii-overall_miss_rate_dcache.jpg")
print("07-ii-overall_miss_rate_dcache.jpg saved")
plt.clf()

plt.figure(figsize=(14,14))
plt.bar(ranks, avg_overall_miss_latency_dcache)
addlabels(ranks, avg_overall_miss_latency_dcache)
plt.xlabel("Rank")
plt.ylabel("Avg Overall Miss Latency (DCache)")
plt.ylim(53000.0, 57800.0)
plt.savefig("plots/07-iii-avg_overall_miss_latency_dcache.jpg")
print("07-iii-avg_overall_miss_latency_dcache.jpg saved")
plt.clf()

plt.figure(figsize=(10,10))
plt.bar(ranks, overall_miss_cycles_icache)
addlabels(ranks, overall_miss_cycles_icache)
plt.xlabel("Rank")
plt.ylabel("Overall Miss Cycles (ICache)")
plt.ylim(565000000, 571500000)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/07-i-overall_miss_cycles_icache.jpg")
print("07-i-overall_miss_cycles_icache.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, overall_miss_rate_icache)
addlabels(ranks, overall_miss_rate_icache)
plt.xlabel("Rank")
plt.ylabel("Overall Miss Rate (ICache)")
plt.ylim(0.040400, 0.040620)
plt.savefig("plots/07-ii-overall_miss_rate_icache.jpg")
print("07-ii-overall_miss_rate_icache.jpg saved")
plt.clf()

plt.figure(figsize=(12,12))
plt.bar(ranks, avg_overall_miss_latency_icache)
addlabels(ranks, avg_overall_miss_latency_icache)
plt.xlabel("Rank")
plt.ylabel("Avg Overall Miss Latency (ICache)")
plt.ylim(16840.0, 16950.0)
plt.savefig("plots/07-iii-avg_overall_miss_latency_icache.jpg")
print("07-iii-avg_overall_miss_latency_icache.jpg saved")
plt.clf()

plt.figure(figsize=(10,10))
plt.bar(ranks, overall_miss_cycles_l2cache)
addlabels(ranks, overall_miss_cycles_l2cache)
plt.xlabel("Rank")
plt.ylabel("Overall Miss Cycles (L2Cache)")
plt.ylim(310000000, 319250000)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/07-i-overall_miss_cycles_l2cache.jpg")
print("07-i-overall_miss_cycles_l2cache.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, overall_miss_rate_l2cache)
addlabels(ranks, overall_miss_rate_l2cache)
plt.xlabel("Rank")
plt.ylabel("Overall Miss Rate (L2Cache)")
plt.ylim(0.122000, 0.126500)
plt.savefig("plots/07-ii-overall_miss_rate_l2cache.jpg")
print("07-ii-overall_miss_rate_l2cache.jpg saved")
plt.clf()

plt.figure(figsize=(14,14))
plt.bar(ranks, avg_overall_miss_latency_l2cache)
addlabels(ranks, avg_overall_miss_latency_l2cache)
plt.xlabel("Rank")
plt.ylabel("Avg Overall Miss Latency (L2Cache)")
plt.ylim(70000.0, 71700.0)
plt.savefig("plots/07-iii-avg_overall_miss_latency_l2cache.jpg")
print("07-iii-avg_overall_miss_latency_l2cache.jpg saved")
plt.clf()

plt.figure(figsize=(10,10))
plt.bar(ranks, rob_reads)
addlabels(ranks, rob_reads)
plt.xlabel("Rank")
plt.ylabel("Number of ROB Accesses (Read)")
plt.ylim(14298000, 14301000)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/08-i-rob_reads.jpg")
print("08-i-rob_reads.jpg saved")
plt.clf()

plt.figure(figsize=(10,12))
plt.bar(ranks, rob_writes)
addlabels(ranks, rob_writes)
plt.xlabel("Rank")
plt.ylabel("Number of ROB Accesses (Write)")
plt.ylim(22701000, 22706000)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/08-ii-rob_writes.jpg")
print("08-ii-rob_writes.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, lsq_full_count)
addlabels(ranks, lsq_full_count)
plt.xlabel("Rank")
plt.ylabel("Number of times LSQ became full, causing stall")
plt.ylim(5000, 7700)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/09-lsq_full_count.jpg")
print("09-lsq_full_count.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, forw_loads_count)
addlabels(ranks, forw_loads_count)
plt.xlabel("Rank")
plt.ylabel("Loads with data forwarded from stores")
plt.ylim(281000, 286025)
plt.savefig("plots/10-forw_loads_count.jpg")
print("10-forw_loads_count.jpg saved")
plt.clf()

plt.figure(figsize=(10,6))
plt.bar(ranks, blocked_cache_count)
addlabels(ranks, blocked_cache_count)
plt.xlabel("Rank")
plt.ylabel("Memory access fails due to cache being blocked")
plt.ylim(200, 360)
plt.locator_params(axis="y", integer=True)
plt.savefig("plots/11-blocked_cache_count.jpg")
print("11-blocked_cache_count.jpg saved")
plt.clf()
