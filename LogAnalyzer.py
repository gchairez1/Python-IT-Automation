"""
=========================================================
LogAnalyzer.py
Author: Gonzalo Chairez

Description:
Analyzes text-based log files and summarizes
the number of ERROR, WARNING, and INFO entries.

Python IT Automation Toolkit
=========================================================
"""

import os

print("=" * 60)
print("               LOG ANALYZER")
print("=" * 60)

log_file = input("Enter log file path: ").strip()

if not os.path.isfile(log_file):
    print("\n[ERROR] File not found.")
    exit()

errors = 0
warnings = 0
infos = 0
total_lines = 0

with open(log_file, "r", encoding="utf-8", errors="ignore") as file:

    for line in file:

        total_lines += 1

        upper = line.upper()

        if "ERROR" in upper:
            errors += 1

        elif "WARNING" in upper:
            warnings += 1

        elif "INFO" in upper:
            infos += 1

print("\n" + "=" * 60)
print("LOG SUMMARY")
print("=" * 60)

print(f"Total Lines : {total_lines}")
print(f"Errors      : {errors}")
print(f"Warnings    : {warnings}")
print(f"Info        : {infos}")

print("=" * 60)

if errors > 0:
    print("\n⚠ Review ERROR entries first.")
else:
    print("\n✔ No ERROR entries detected.")
