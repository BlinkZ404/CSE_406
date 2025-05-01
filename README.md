# CSE 406 - Operating System Lab

![OS Banner](https://img.shields.io/badge/CSE%20406-Operating%20System%20Lab-blue)

This repository contains implementations of fundamental operating system algorithms for CSE 406 Operating System Lab.

🔗 **Repository: [https://github.com/BlinkZ404/CSE_406.git](https://github.com/BlinkZ404/CSE_406.git)**

## 📋 File Structure

## 🖥️ CPU Scheduling Algorithms

| Algorithm   | File                                                             | Description                                                      |
|-------------|------------------------------------------------------------------|------------------------------------------------------------------|
| FCFS        | [lab_2_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_2_cw.py) | First-Come, First-Served: Non-preemptive scheduling based on arrival time |
| SJF         | [lab_3_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_3_cw.py) | Shortest Job First: Selects process with smallest execution time |
| Round Robin | [lab_4_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_4_cw.py) | Allocates fixed time slices to each process in a circular queue  |
| Priority    | [lab_5_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_5_cw.py) | Allocates CPU based on process priority values                  |

## 💾 Disk Scheduling Algorithms

| Algorithm   | File                                                             | Description                                                      |
|-------------|------------------------------------------------------------------|------------------------------------------------------------------|
| FCFS        | [lab_6_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_6_cw.py) | Services disk requests in order of arrival                       |
| SSTF        | [lab_7_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_7_cw.py) | Shortest Seek Time First: Selects request with least head movement |
| SCAN        | [lab_8_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_8_cw.py) | Moves disk arm in one direction until end, then reverses |
| C-SCAN      | [lab_9_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_9_cw.py) | Circular SCAN: Services requests in one direction, jumps back to beginning at end |

## 🧠 Page Replacement Algorithms

| Algorithm   | File                                                              | Description                                                      |
|-------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| FIFO        | [lab_10_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_10_cw.py) | First-In, First-Out: Replaces oldest page in memory              |
| LRU         | [lab_11_cw.py](https://github.com/BlinkZ404/CSE_406/blob/main/lab_11_cw.py) | Least Recently Used: Replaces page unused for longest time       |

## 🔧 Usage

Each file contains a self-contained implementation. Run any Python file directly:

```bash
python lab_2_cw.py
```
