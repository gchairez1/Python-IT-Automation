"""
=========================================================
FileHasher.py
Author: Gonzalo Chairez

Description:
Calculates MD5, SHA1, and SHA256 hashes
for any file.

Python IT Automation Toolkit
=========================================================
"""

import hashlib
import os

print("=" * 60)
print("              FILE HASH CALCULATOR")
print("=" * 60)

filepath = input("Enter file path: ").strip()

if not os.path.isfile(filepath):
    print("\n[ERROR] File not found.")
    exit()

def calculate_hash(filename, algorithm):

    hasher = algorithm()

    with open(filename, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()


print("\nCalculating hashes...\n")

md5 = calculate_hash(filepath, hashlib.md5)
sha1 = calculate_hash(filepath, hashlib.sha1)
sha256 = calculate_hash(filepath, hashlib.sha256)

print("=" * 60)

print("MD5")
print(md5)

print("\nSHA1")
print(sha1)

print("\nSHA256")
print(sha256)

print("=" * 60)

print("\nHash calculation completed successfully.")
