def fcfs_disk_scheduling(requests, head_start):
    print("FCFS Disk Scheduling\n")
    print(f"Initial Head Position: {head_start}\n")
    
    total_head_movement = 0
    current_position = head_start

    print(f"{'From':<10}{'To':<10}{'Movement':<10}")
    print("-" * 30)

    for req in requests:
        movement = abs(req - current_position)
        print(f"{current_position:<10}{req:<10}{movement:<10}")
        total_head_movement += movement
        current_position = req

    print("-" * 30)
    print(f"{'Total Movement:':<20}{total_head_movement}")
    print(f"{'Average Movement:':<20}{total_head_movement / len(requests):.2f}")

requests = [176, 79, 34, 60, 92, 11, 41, 114]
head_start = 50
fcfs_disk_scheduling(requests, head_start)