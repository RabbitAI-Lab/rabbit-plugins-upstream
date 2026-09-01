#!/usr/bin/env python3
"""Emit the mcp_servers fragment for a remote Mac bridged via cua-driver over SSH.

Run on the AGENT'S host (the server). Prints YAML suitable for
~/.hermes/config.yaml under `mcp_servers:` (indent to that level).

REQUIRED env:  MAC_USER   (the macOS account on the Mac)
OPTIONAL env:  REVERSE_PORT (default 2299)   REMOTE_KEY (default ~/.ssh/id_ed25519_mac)
               MAC_CUA     (default /Users/<MAC_USER>/.local/bin/cua-driver)
               SERVER_NAME (default mac_computer)
"""
import os, sys
rev = os.environ.get("REVERSE_PORT", "2299")
key = os.environ.get("REMOTE_KEY", "~/.ssh/id_ed25519_mac")
mac_user = os.environ.get("MAC_USER", "")
name = os.environ.get("SERVER_NAME", "mac_computer")
if not mac_user:
    print("ERROR: set MAC_USER to the macOS account on the Mac, e.g.  MAC_USER=alice", file=sys.stderr)
    sys.exit(1)
mac_cua = os.environ.get("MAC_CUA", f"/Users/{mac_user}/.local/bin/cua-driver")

key = key.replace("~", os.path.expanduser("~"))

def yaml_quote(s):
    if any(c.isspace() for c in s):
        return repr(s)
    return s

args = ["-T", "-p", rev,
        "-o", "BatchMode=yes",
        "-o", "StrictHostKeyChecking=accept-new",
        "-o", "ServerAliveInterval=30",
        "-o", "ServerAliveCountMax=3",
        "-i", key,
        f"{mac_user}@127.0.0.1",
        mac_cua, "mcp"]

print(f"  {name}:")
print("    command: /usr/bin/ssh")
print("    args:")
for a in args:
    print(f"    - {yaml_quote(a)}")
print("    enabled: true")
print()
print("# For other agents, the same command/args map to that client's stdio MCP form.")
print("# Hermes CLI: run '/reload-mcp' or start a NEW session after adding this.")
