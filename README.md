The benchmark program assigned for simulation is "qsort5.c". It has been compiled using `gcc qsort5.c -S -o qsort5 -lpthread`. Its execution is simulated with the gem5 simulator system across multiple varying parameters. 

To run the config script for the top 10 configurations, do the following:
    - Download the compressed file and unzip it in '~/gem5/configs/' directory
    - In the terminal, `cd` into this folder, and run the command: `export CODE=$(pwd)`
    - Go to the gem5 root directory in the same terminal
    - Run the command: `build/X86/gem5.opt ${CODE}/config.py --cmd=${CODE}/qsort5 --rank=X`, where X is any rank between 1 to 10
    - Change the value of the rank argument to run the simulation for the top 10 configurations
    - The output is stored in m5out folder present in the directory

To run the config script for a custom configuration, along with the other steps above, run the command `build/X86/gem5.opt ${CODE}/config.py --cmd=${CODE}/qsort5 --args=XXXXXXXX`, where each X is either 1 or 2, the first or second value available for the following parameters in order:
LQ_ENTRIES: [32, 64]
SQ_ENTRIES: [32, 64]
L1D_SIZE: ['32kB', '64kB']
L1I_SIZE: ['8kB', '16kB']
L2_SIZE: ['256kB', '512kB']
BP_TYPE: [TournamentBP, BiModeBP]
ROB_ENTRIES: [128, 192]
IQ_ENTRIES: [16, 64]

The 'stats.txt' for the top 10 configurations is stored in 'm5out/rank-N_args-A_stats.txt', where N is the rank and A is the argument of the corresponding configuration.

The config script is simulated on gem5 version 22.1.0.0, with global frequency set at 1000000000000 ticks per second.