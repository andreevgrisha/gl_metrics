# python3 gathering metrics script

import sys
import psutil

# check args from command line
if len (sys.argv) < 2:
    print ('wrong argument, will try "metrics cpu" or "metrics mem" commands')
# if arg = cpu, print CPU metrics:
elif sys.argv[1] == "cpu":
    cpu = psutil.cpu_times_percent(interval=1)
    print("CPU LOADING INFO:")
    print('cpu.idle: ', cpu[3])
    print('cpu.user: ', cpu[0])
    print('cpu.guest: ', cpu[8])
    print('cpu.iowait: ', cpu[4])
    print('cpu.steal: ', cpu[7])
    print('cpu.system: ', cpu[2])
# if arg = mem, print memory  metrics:
elif sys.argv[1] == "mem":
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    print("MEMORY LOADING INFO:")
    print('mem.total: ', mem[0])
    print('mem.used: ', mem[3])
    print('mem.free: ', mem[4])
    print('mem.shared: ', mem[9])
    print('swap.total: ', mem[0])
    print('swap.used: ', mem[1])
    print('swap.free: ', mem[2])
# other way print help
else:
    print ('wrong argument, will try "metrics cpu" or "metrics mem" commands')
    
