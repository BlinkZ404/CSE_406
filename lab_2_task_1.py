def fcfs_sc(processes):
    processes.sort(key = lambda x : x[1])

    n = len(processes)
    ct, tat, wt = [0] * n, [0] * n, [0] *n

    ct[0] = processes[0][1] + processes[0][2]
    for i in range(1,n):
        ct[i] = max(ct[i-1], processes[i][1]) + processes[i][2]

    for i in range(n):
        tat[i] = ct[i] - processes[i][1]
        wt[i] = tat[i] - processes[i][2]

    avg_wt = sum(wt)/n
    avg_tat = sum(tat)/n
    
    print("ID | AT | BT | CT | TAT | WT") #AT = Arrival Time, BT = Burst Time, CT = Completion Time, TAT = Turnover Around Time, WT = Waiting Time
    for i in range(n):
        print(f"{processes[i][0]}  | {processes[i][1]}  | {processes[i][2]}  | {ct[i]}  | {tat[i]}   | {wt[i]}")

    print(f"\nAvg WT: {avg_wt: .2f} \nAvg TAT: {avg_tat: .2f}")

processes = [(0,2,5), (1,0,3), (2,4,4)]
fcfs_sc(processes)