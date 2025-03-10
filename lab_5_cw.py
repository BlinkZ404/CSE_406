def priority_scheduling(processes, time_quantum):
    time, completed, n = 0, 0 , len(processes)
    remaining_bt = {p[0]: p[3] for p in processes}
    processes.sort(key=lambda x: (x[2], -x[1]))
    process_info = {}
    execution_order = []

    while completed < n:
        ready_queue = [p for p in processes if p[2] <= time and remaining_bt[p[0]] >0]
        if ready_queue:
            process = max(ready_queue, key=lambda x: x[1])
            pid = process[0]
            execution_order.append(pid)
            exec_time = min(time_quantum, remaining_bt[pid])
            remaining_bt[pid] -= exec_time
            time += exec_time

            if remaining_bt[pid] == 0:
                completed += 1
                process_info[pid] = [pid, process[1], process[2], process[3], time, time - process[2], (time - process[2]) - process[3]]
        else:
            time += 1

    print("Execution Order:", " -> ".join(map(str, execution_order))) 
    print("\nPID\tPR\tAT\tBT\tCT\tTAT\tWT") 
    for p in sorted(process_info.values()):
        print("\t".join(map(str, p))) 

process_list = [(1,10,0,5), (2,20,1,4), (3,30,3,2), (4,40,4,1)]
time_quantum = 2
priority_scheduling(process_list, time_quantum) 