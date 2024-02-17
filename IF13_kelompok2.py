"""
APLIKASI ALOGRITMA PENJADWALAN DISK
Disk Scheduler Algorithm Aplication

IF 13 - Kelompok 2
10122905 - Rayhandhika Yusuf
10122907 - Vina Lestari
10122911 - Tetta Trisky T
"""

import streamlit as st
import matplotlib.pyplot as plt

def FCFS(arr, head, size):
    seek_count = 0;
    distance, cur_track = 0, 0;
    arr.append(head)
    for i in range(size+1):
        cur_track = arr[i];
        distance = abs(cur_track - arr[i-1]);
        seek_count += distance;
    return seek_count, arr

# Calculates difference of each track number with the head position
def calculate_difference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)

# find unaccessed track which is at minimum distance from head
def find_min(diff):
    index = -1
    minimum = 999999999
    for i in range(len(diff)):
        if not diff[i][1] and minimum > diff[i][0]:
            minimum = diff[i][0]
            index = i
    return index

def SSTF(request, head):
    if not request:
        return
    l = len(request)
    diff = [[0, False] for _ in range(l)]
    seek_count = 0
    seek_sequence = [0] * (l + 1)
    for i in range(l):
        seek_sequence[i] = head
        calculate_difference(request, head, diff)
        index = find_min(diff)
        diff[index][1] = True
        seek_count += diff[index][0]
        head = request[index]
    seek_sequence[l] = head
    return seek_count, seek_sequence

def SCAN(arr, head, direction):
    seek_count = 0
    seek_sequence = []
    arr = sorted(arr)
    if direction == "left":
        seek_sequence = arr[::-1] + arr[arr.index(head)+1:] + [head]
    else:
        seek_sequence = arr[:arr.index(head)] + arr[arr.index(head):]
    for i in range(len(seek_sequence)-1):
        seek_count += abs(seek_sequence[i] - seek_sequence[i+1])
    return seek_count, seek_sequence

def CSCAN(arr, head):
    seek_count = 0
    distance = 0
    cur_track = 0
    left = []
    right = []
    seek_sequence = []
    left.append(0)
    right.append(size - 1)
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
    left.sort()
    right.sort()
    for i in range(len(right)):
        cur_track = right[i]
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track
    head = 0
    seek_count += (size - 1)
    for i in range(len(left)):
        cur_track = left[i]
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track
    return seek_count, seek_sequence

if __name__ == '__main__':
    # request array
    arr = [155, 100, 210, 105, 50, 390, 80, 260, 38, 384]
    with st.sidebar:
        st.header("Input Parameters Need")
        size = st.number_input("Enter disk size:", min_value=1, max_value=8, step=1)
        head = st.number_input("Enter starting head position:", min_value=0, step=1)
        st.caption('IF13 - Kelompok 2')
        st.caption('10122905 - Rayhandhika Yusuf')
        st.caption('10122907 - Vina Lestari')
        st.caption('10122911 - Tetta Trisky T')
        st.caption('Created At 2023')

    colors = {
        "FCFS": "#642c6c",
        "SSTF": "#d55861",
        "SCAN": "#ab3c6c",
        "CSCAN": "#ecb484"
    }

    seek_count, arr = FCFS(arr, head, size)
    sstf_seq, sstf_seek = SSTF(arr, head)
    scan_seq, scan_seek = SCAN(arr, head, "right")
    seek_count, seek_sequence = CSCAN(arr, head)
    
    # create plot chart with line
    fig, ax = plt.subplots()
    ax.plot([i for i in range(len(arr))], arr, marker="o", linestyle="-", color=colors["FCFS"], label="FCFS")
    ax.plot([i for i in range(len(sstf_seek))], sstf_seek, marker="o", linestyle="-", color=colors["SSTF"], alpha=0.3, label="SSTF")
    ax.plot([i for i in range(len(scan_seek))], scan_seek, marker="o", linestyle="-", color=colors["SCAN"], alpha=0.7, label="SCAN")
    ax.plot([i for i in range(len(seek_sequence))], seek_sequence, marker="o", linestyle="-", color=colors["CSCAN"], label="C-SCAN")

    ax.set_xlabel("Head Position")
    ax.set_ylabel("Track Number")
    ax.set_title("FCFS - SSTF - SCAN - CSAN Disk Scheduling Algorithm")

    ax.legend(loc = "upper left", fontsize = 'small')
    st.pyplot(fig)