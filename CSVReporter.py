"""
=========================================================
CSVReporter.py
Author: Gonzalo Chairez

Description:
Reads a CSV file and generates a summary
report including row counts, columns,
missing values, duplicates, and sample data.

Python IT Automation Toolkit
=========================================================
"""

import pandas as pd
import os

print("=" * 60)
print("               CSV REPORTER")
print("=" * 60)

filepath = input("Enter CSV file path: ").strip()

if not os.path.isfile(filepath):
    print("\n[ERROR] File not found.")
    exit()

try:
    df = pd.read_csv(filepath)

except Exception as e:
    print("\nUnable to read CSV.")
    print(e)
    exit()

print("\n" + "=" * 60)
print("CSV SUMMARY")
print("=" * 60)

print(f"Rows           : {len(df)}")
print(f"Columns        : {len(df.columns)}")

print("\nColumn Names")

for column in df.columns:
    print(f" • {column}")

print("\nMissing Values")

missing = df.isnull().sum()

for column, count in missing.items():
    print(f"{column:<20} {count}")

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows : {duplicates}")

print("\nFirst Five Records")

print(df.head())

print("\n" + "=" * 60)

report_name = "CSV_Report.txt"

with open(report_name, "w") as report:

    report.write("CSV REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write(f"Rows: {len(df)}\n")
    report.write(f"Columns: {len(df.columns)}\n")
    report.write(f"Duplicate Rows: {duplicates}\n\n")

    report.write("Columns\n")

    for column in df.columns:
        report.write(f"- {column}\n")

print(f"\nSummary report saved as {report_name}")
