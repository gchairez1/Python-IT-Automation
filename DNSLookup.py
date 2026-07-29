"""
=========================================================
DNSLookup.py
Author: Gonzalo Chairez

Description:
Performs DNS lookups for a domain,
including IPv4, IPv6, and Reverse DNS.

Python IT Automation Toolkit
=========================================================
"""

import socket

print("=" * 60)
print("                 DNS LOOKUP TOOL")
print("=" * 60)

domain = input("Enter a domain (example: google.com): ").strip()

try:

    print("\nResolving hostname...")

    ipv4 = socket.gethostbyname(domain)

    print(f"\nIPv4 Address : {ipv4}")

except socket.gaierror:

    print("\nUnable to resolve hostname.")
    exit()

print("\n" + "-" * 60)

try:

    hostname, aliases, addresses = socket.gethostbyname_ex(domain)

    print("Hostname")
    print(hostname)

    print("\nAliases")

    if aliases:
        for alias in aliases:
            print(f" • {alias}")
    else:
        print(" None")

    print("\nIPv4 Addresses")

    for ip in addresses:
        print(f" • {ip}")

except socket.error:
    print("Unable to retrieve hostname information.")

print("\n" + "-" * 60)

try:

    info = socket.getaddrinfo(domain, None, socket.AF_INET6)

    print("IPv6 Addresses")

    ipv6_addresses = sorted({entry[4][0] for entry in info})

    if ipv6_addresses:
        for ip in ipv6_addresses:
            print(f" • {ip}")
    else:
        print(" None Found")

except socket.gaierror:
    print("IPv6 Addresses")
    print(" None Found")

print("\n" + "-" * 60)

try:

    reverse = socket.gethostbyaddr(ipv4)

    print("Reverse DNS")

    print(f"Hostname : {reverse[0]}")

except socket.herror:

    print("Reverse DNS")
    print("No PTR Record Found")

print("\n" + "=" * 60)
print("Lookup Complete")
print("=" * 60)
