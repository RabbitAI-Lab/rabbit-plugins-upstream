#!/usr/bin/env python3
"""
bq.py -- thin client for the engram-serve warm daemon.

Usage: python3 engram/bq.py <command> [args...]   (identical to engram.py's CLI)

Tries the Unix socket at /tmp/engram-serve.sock first (fast path, warm
model + matrix in the daemon). If the socket is missing, refused, or the
daemon errors out for any reason, falls straight back to a plain
`python3 engram/engram.py <same args>` subprocess so this command always
works regardless of daemon health. Output is passed through unmodified.
"""

import json
import os
import socket
import subprocess
import sys

# Engram: load socket path from config
try:
    import bpconfig
    SOCK_PATH = bpconfig.socket_path()
except Exception:
    SOCK_PATH = "/tmp/engram-serve.sock"

ENGRAM_DIR = os.path.dirname(os.path.abspath(__file__))
ENGRAM_PATH = os.path.join(ENGRAM_DIR, "engram.py")


def try_daemon(argv):
    """Return output string on success, or None to signal fallback."""
    if not os.path.exists(SOCK_PATH):
        return None
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(15.0)
        sock.connect(SOCK_PATH)
    except OSError:
        return None

    try:
        cmd = argv[0] if argv else ""
        req = {"cmd": cmd, "argv": argv[1:]}
        sock.sendall(json.dumps(req).encode("utf-8"))
        sock.shutdown(socket.SHUT_WR)

        chunks = []
        while True:
            data = sock.recv(65536)
            if not data:
                break
            chunks.append(data)
        raw = b"".join(chunks)
        if not raw:
            return None
        reply = json.loads(raw.decode("utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return None
    finally:
        try:
            sock.close()
        except OSError:
            pass

    if not reply.get("ok"):
        return None
    return reply


def fallback(argv):
    os.execvp(sys.executable, [sys.executable, ENGRAM_PATH] + argv)


def main():
    argv = sys.argv[1:]
    reply = try_daemon(argv)
    if reply is None:
        fallback(argv)  # never returns
        return
    sys.stdout.write(reply["output"])
    sys.stdout.flush()
    sys.exit(reply.get("exit_code", 0))


if __name__ == "__main__":
    main()
