def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    next_replace = 0

    print(f"{'Step':<5} {'Page':<5} {'Memory':<20} {'Fault'}")
    print("-" * 40)

    for step, page in enumerate(pages, 1):
        fault = "No"
        if page not in memory:
            fault = "Yes"
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory[next_replace] = page
                next_replace = (next_replace + 1) % capacity
            page_faults += 1
        print(f"{step:<5} {page:<5} {str(memory):<20} {fault}")

    print("-" * 40)
    print(f"Total Page Faults: {page_faults}")


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
capacity = 3
fifo_page_replacement(pages, capacity)