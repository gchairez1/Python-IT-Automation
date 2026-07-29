"""
=========================================================
PortScanner.py
Author: Gonzalo Chairez

Description:
A simple TCP port scanner that checks the
most common ports on a target host.

Python IT Automation Toolkit
=========================================================
"""

import socket
import time

print("=" * 55)
print("             PYTHON PORT SCANNER")
print("=" * 55)

target = input("Enter IP address or hostname: ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n[ERROR] Unable to resolve hostname.")
    exit()

print(f"\nScanning: {target} ({target_ip})")

common_ports = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate"
}

start = time.time()

print("\nOpen Ports")
print("-" * 55)

open_count = 0

for port, service in common_ports.items():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"[OPEN]  Port {port:<5} {service}")
        open_count += 1

    sock.close()

elapsed = round(time.time() - start, 2)

print("\n" + "=" * 55)
print(f"Scan Complete")
print(f"Target      : {target_ip}")
print(f"Ports Found : {open_count}")
print(f"Time Elapsed: {elapsed} seconds")
print("=" * 55)
