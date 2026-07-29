"""
=========================================================
SystemHealthDashboard.py
Author: Gonzalo Chairez

Description:
A live system monitoring dashboard displaying
CPU, Memory, Disk, Network, Uptime, and
Running Processes.

Python IT Automation Toolkit
=========================================================
"""

import psutil
import socket
import platform
import os
import time
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_uptime():

    boot = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()

    delta = now - boot

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60

    return f"{days} Days {hours} Hours {minutes} Minutes"


def internet_connected():

    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return "Connected"
    except OSError:
        return "Disconnected"


while True:

    clear_screen()

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    processes = len(psutil.pids())

    hostname = socket.gethostname()

    ip = socket.gethostbyname(hostname)

    print("=" * 65)
    print("            PYTHON SYSTEM HEALTH DASHBOARD")
    print("=" * 65)

    print(f"Computer Name      : {hostname}")
    print(f"Operating System   : {platform.system()} {platform.release()}")

    print("-" * 65)

    print(f"CPU Usage          : {cpu}%")
    print(f"Memory Usage       : {memory.percent}%")

    print(
        f"Memory Available   : "
        f"{round(memory.available / (1024 ** 3), 2)} GB"
    )

    print(f"Disk Usage         : {disk.percent}%")

    print(
        f"Free Disk Space    : "
        f"{round(disk.free / (1024 ** 3), 2)} GB"
    )

    print("-" * 65)

    print(f"Running Processes  : {processes}")
    print(f"IP Address         : {ip}")
    print(f"Network Status     : {internet_connected()}")
    print(f"System Uptime      : {get_uptime()}")

    print("=" * 65)
    print("Refreshing every 5 seconds... (Ctrl+C to quit)")
    print("=" * 65)

    try:
        time.sleep(5)

    except KeyboardInterrupt:
        print("\nDashboard stopped.")
        break
