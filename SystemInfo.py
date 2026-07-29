import platform
import socket
import psutil

print("=" * 50)
print("WINDOWS SYSTEM INFORMATION")
print("=" * 50)

print(f"Computer Name : {socket.gethostname()}")
print(f"Operating Sys : {platform.system()} {platform.release()}")
print(f"Processor     : {platform.processor()}")

memory = psutil.virtual_memory()

print(f"RAM Installed : {round(memory.total/1024**3,2)} GB")
print(f"RAM Used      : {memory.percent}%")

disk = psutil.disk_usage('/')

print(f"Disk Usage    : {disk.percent}%")
print(f"Free Space    : {round(disk.free/1024**3,2)} GB")

print("=" * 50)
