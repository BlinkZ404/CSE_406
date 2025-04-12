def c_scan(requests, head, disk_size=199):
    total_seek = 0
    sequence = []

    if 0 not in requests:
        requests.append(0)
    if disk_size not in requests:
        requests.append(disk_size)
    
    requests = sorted(set(requests))

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    for r in right:
        total_seek += abs(head - r)
        sequence.append(r)
        head = r
    
    if left:
        head = 0
        
        for r in left:
            total_seek += abs(head - r)
            sequence.append(r)
            head = r
    
    return total_seek, sequence

if __name__ == "__main__":
    requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
    head = 53
    disk_size = 199

    if head in requests:
        requests.remove(head)

    total_seek, seq = c_scan(requests, head, disk_size)

    print("Seek Sequence:", [head] + seq)
    print("Total Seek Time:", total_seek)
