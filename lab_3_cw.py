def sjf_scheduling(processes):
    processes.sort(key=lambda x: x["arrival_time"])
    time, completed = 0, []

    while processes:
        available = [p for p in processes if p["arrival_time"] <= time]
        
        if not available:
            time = processes[0]["arrival_time"]
            available = [processes[0]]

        shortest = min(available, key=lambda x: x["burst_time"])
        processes.remove(shortest)

        time += shortest["burst_time"]
        completed.append({
            "pid": shortest["pid"],
            "arrival_time": shortest["arrival_time"],
            "burst_time": shortest["burst_time"],
            "completion_time": time,
            "turnaround_time": time - shortest["arrival_time"],
            "waiting_time": time - shortest["arrival_time"] - shortest["burst_time"]
        })

    return completed


processes = [
    {"pid": "P1", "burst_time": 6, "arrival_time": 2},
    {"pid": "P2", "burst_time": 2, "arrival_time": 5},
    {"pid": "P3", "burst_time": 8, "arrival_time": 1},
    {"pid": "P4", "burst_time": 3, "arrival_time": 0},
    {"pid": "P5", "burst_time": 4, "arrival_time": 4}
]

print("PID  Arrival  Burst  Completion  Turnaround  Waiting")
for p in sjf_scheduling(processes):
    print(f"{p['pid']:3}  {p['arrival_time']:7}  {p['burst_time']:5}  {p['completion_time']:10}  {p['turnaround_time']:9}  {p['waiting_time']:6}")
