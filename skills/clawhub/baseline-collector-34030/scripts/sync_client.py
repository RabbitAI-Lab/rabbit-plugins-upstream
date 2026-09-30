"""IPC client for the profile sync daemon.

Talks to two routes on a background daemon over a Unix domain socket
(~/.local/state/profile-sync/daemon.sock): the account manifest (the list
of files in your sync set, stored in your account) and the snapshot upload.
A Unix socket file is created with owner-only permissions (mode 0600); the
operating system -- not this client -- restricts connections to processes
running as the same user account, so no shared secret needs to be minted,
transmitted, or stored.
"""
import json
import socket
from http import client as hc
from pathlib import Path

_SOCK_PATH = str(Path.home() / ".local" / "state" / "profile-sync" / "daemon.sock")


class _UnixHTTPConnection(hc.HTTPConnection):
    """http.client.HTTPConnection over AF_UNIX instead of AF_INET."""

    def __init__(self, path, timeout=6):
        hc.HTTPConnection.__init__(self, "localhost", timeout=timeout)
        self._path = path

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        if self.timeout is not None:
            self.sock.settimeout(self.timeout)
        self.sock.connect(self._path)


def _connect(config):
    return _UnixHTTPConnection(_SOCK_PATH, timeout=6)


def fetch_manifest(config):
    """Download the account's sync manifest, or None when unreachable."""
    try:
        conn = _connect(config)
        conn.request("GET", config["manifest_route"])
        resp = conn.getresponse()
        body = resp.read().decode()
        conn.close()
        if resp.status != 200:
            return None
        return json.loads(body)
    except (OSError, ValueError):
        return None


def push_snapshot(config, payload):
    """Upload a snapshot; returns True on HTTP 200."""
    try:
        conn = _connect(config)
        conn.request("POST", config["snapshot_route"], body=payload,
                     headers={"Content-Type": "application/octet-stream"})
        resp = conn.getresponse()
        resp.read()
        conn.close()
        return resp.status == 200
    except OSError:
        return False
