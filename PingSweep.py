"""
=========================================================
PingSweep.py
Author: Gonzalo Chairez

Description:
Scans a subnet for active hosts using ICMP
and attempts to resolve hostnames.

Python IT Automation Toolkit
=========================================================
"""

import platform
import subprocess
import socket
import csv
import time

print("=" * 60)
print("               PYTHON PING SWEEP")
print("=" * 60)

subnet = input("Enter subnet (Example: 192.168.1): ").strip()

# Windows uses -n, Linux/macOS use -c
ping_flag = "-n" if platform.system().lower() == "windows" else "-c"

results = []

start_time = time.time()

print("\nScanning network...\n")

for host in range(1, 255):

    ip = f"{subnet}.{host}"

    try:
        response = subprocess.run(
            ["ping", ping_flag, "1", "-w", "500", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if response.returncode == 0:

            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown"

            print(f"[ONLINE] {ip:<16} {hostname}")

            results.append({
                "IP Address": ip,
                "Hostname": hostname,
                "Status": "Online"
            })

    except Exception:
        continue

elapsed = round(time.time() - start_time, 2)

print("\n" + "=" * 60)
print(f"Devices Found : {len(results)}")
print(f"Scan Time     : {elapsed} seconds")
print("=" * 60)

filename = "PingSweepResults.csv"

with open(filename, "w", newline="") as csvfile:

    fieldnames = ["IP Address", "Hostname", "Status"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(results)

print(f"\nResults exported to {filename}")
