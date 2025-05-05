def fifo_pr(pages,capacity):
    memory = []
    index = 0
    page_faults = 0
    hits = 0

    for page in pages:
        if page in memory:
            hits += 1
            print(f"Page {page}: Hit -> {memory}")
        else:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % capacity
            print(f"Page {page}: Miss -> {memory}")

    print(f"\nTotal Miss: {page_faults}")
    print(f"Total Hits: {hits}")

pages = [0, 1, 5, 3, 5, 0, 2, 4, 7, 9, 0, 0, 3]
capacity = 4
fifo_pr(pages, capacity)
