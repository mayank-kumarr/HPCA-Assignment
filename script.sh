#!/bin/bash
set -e

OUTDIR=output/
EXEC=~/gem5/build/X86/gem5.opt
SCRIPT=config.py
CMD=qsort5

# 0 - LQ_ENTRIES = [32, 64]
# 1 - SQ_ENTRIES = [32, 64]
# 2 - L1D_SIZE = ['32kB', '64kB']
# 3 - L1I_SIZE = ['8kB', '16kB']
# 4 - L2_SIZE = ['256kB', '512kB']
# 5 - BP_TYPE = [TournamentBP, BiModeBP]
# 5 - ROB_ENTRIES = [128, 192]
# 7 - IQ_ENTRIES = [16, 64]

SIZE=(2 2 2 2 2 2 2 2) # Sizes in reverse
TOTAL=256
for (( i=0; i<256; i++ ))
do
    args=""
    valCpy=$i
    for s in "${SIZE[@]}"
    do
        rem=$(( $valCpy % $s ))
        rem=$(( $rem + 1 ))
        valCpy=$(( $valCpy / $s )) 
        args="${rem}${args}"
    done
    ${EXEC} --outdir=${OUTDIR}num-${i}_args-${args} ${SCRIPT} --cmd=${CMD} --args=${args}
    echo "Sim Number ${i} Done"
done
