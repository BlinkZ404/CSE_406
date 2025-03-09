from collections import deque

def round_robin(processes, quantum):
    processes.sort(key=lambda x: x["arrival"]) 
    queue, time = deque(), 0
    remaining = {p["id"]: p["burst"] for p in processes}
    comp, tat, wt = {}, {}, {}

    i = 0
    while queue or i < len(processes):
        while i < len(processes) and processes[i]["arrival"] <= time:
            queue.append(processes[i]["id"])
            i += 1

        if queue:
            pid = queue.popleft()
            execute = min(quantum, remaining[pid])
            remaining[pid] -= execute
            time += execute

            while i < len(processes) and processes[i]["arrival"] <= time:
                queue.append(processes[i]["id"])
                i += 1

            if remaining[pid] > 0:
                queue.append(pid)
            else:
                comp[pid] = time
                tat[pid] = comp[pid] - next(p["arrival"] for p in processes if p["id"] == pid)
                wt[pid] = tat[pid] - next(p["burst"] for p in processes if p["id"] == pid)
        else:
            time = processes[i]["arrival"]

    print("\n Pid | Arrival | Burst | Completion | Turnaround | Waiting ")
    print("-" * 60)
    for p in processes:
        print(f" {p['id']:3} | {p['arrival']:7} | {p['burst']:5} | {comp[p['id']]:10} | {tat[p['id']]:10} | {wt[p['id']]:7}")

processes = [
    {"id": 1, "burst": 5, "arrival": 0},
    {"id": 2, "burst": 4, "arrival": 1},
    {"id": 3, "burst": 2, "arrival": 2},
    {"id": 4, "burst": 1, "arrival": 4}
]
quantum = 2

round_robin(processes, quantum)
