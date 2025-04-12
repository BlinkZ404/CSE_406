def sstf(requests, head):
    requests = sorted(requests)
    total_seek = 0
    sequence = []

    while requests:
        closest = min(requests, key=lambda x: abs(x - head))
        total_seek += abs(closest - head)
        sequence.append(closest)
        head = closest
        requests.remove(closest)

    return total_seek, sequence

if __name__ == "__main__":
    requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
    head = 53

    if head in requests:
        requests.remove(head)

    total_seek, seek_sequence = sstf(requests, head)

    print("Seek Sequence:", [head] + seek_sequence)
    print("Total Seek Time:", total_seek)
