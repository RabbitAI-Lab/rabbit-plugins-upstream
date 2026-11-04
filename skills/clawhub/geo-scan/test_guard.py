#!/usr/bin/env python3
"""Guard tests for geo-scan — run: python3 test_guard.py

No network and no sockets to non-public hosts are involved: the DNS answers are
supplied by a stub resolver, so what these check is the decision geo-scan makes
about an address and the address it would hand to the socket. Exit 0 = all pass.
"""
import ipaddress
import socket
import sys

import geo_scan as gs

REFUSE = [
    "127.0.0.1", "127.5.5.5", "::1", "0.0.0.0", "10.0.0.1", "172.16.9.9",
    "192.168.1.1", "169.254.169.254", "169.254.255.254", "100.64.0.1",
    "100.127.255.255", "192.0.2.1", "198.51.100.7", "203.0.113.9", "224.0.0.1",
    "239.10.10.10", "240.0.0.1", "fd00::1", "fe80::1", "ffff::",
    "::ffff:127.0.0.1", "::ffff:10.0.0.1", "2002:7f00:0001::",       # 6to4 -> 127.0.0.1
    "2002:0a00:0001::",                                                  # 6to4 -> 10.0.0.1
    "2001:0000:4136:e378:8000:63bf:3fff:fdd2",                        # Teredo, client IPv4
]
ACCEPT = ["93.184.216.34", "8.8.8.8", "1.1.1.1", "2606:4700:4700::1111",
          "2a00:1450:4008:801::200e"]

fails = []

for s in REFUSE:
    if gs.ip_is_public(ipaddress.ip_address(s)):
        fails.append(f"ip_is_public accepted {s}")
for s in ACCEPT:
    if not gs.ip_is_public(ipaddress.ip_address(s)):
        fails.append(f"ip_is_public refused {s}")

# literal hosts go through the same decision, without DNS
for s in ["127.0.0.1", "169.254.169.254", "10.0.0.1"]:
    try:
        gs.resolve_public_ips(s, 80)
        fails.append(f"resolve_public_ips dialled literal {s}")
    except gs.Skipped:
        pass

# a host that answers publicly once and privately afterwards (DNS rebinding):
# the guard is asked again at connect time, so the private answer is what it sees
answers = [(2, "93.184.216.34"), (2, "127.0.0.1"), (2, "169.254.169.254")]
real = socket.getaddrinfo
seq = iter(answers)


def stub(host, port, *a, **k):
    fam, ip = next(seq)
    return [(fam, 1, 6, "", (ip, port))]


socket.getaddrinfo = stub
try:
    if gs.resolve_public_ips("rebind.test", 80) != [(4, "93.184.216.34")]:
        fails.append("first DNS answer was not the public address")
    for i in (2, 3):
        try:
            gs.resolve_public_ips("rebind.test", 80)
            fails.append(f"rebinding answer #{i} was accepted")
        except gs.Skipped:
            pass
finally:
    socket.getaddrinfo = real

# a refused host never reaches the socket layer
try:
    gs.scan("http://127.0.0.1:9/", max_pages=1, budget=10)
    fails.append("scan() accepted a loopback root")
except gs.ScanError as e:
    if "private" not in str(e):
        fails.append(f"loopback refusal said something odd: {e}")

# and a non-http scheme is refused before anything is opened
try:
    gs.Scanner("file:///etc/passwd", 30, True, None)
    fails.append("Scanner accepted a file:// root")
except gs.ScanError:
    pass

print(f"geo-scan {gs.__version__} guard tests: "
      f"{len(REFUSE) + len(ACCEPT) + 6 - len(fails)} passed, {len(fails)} failed")
for f in fails:
    print("  FAIL", f)
sys.exit(1 if fails else 0)
