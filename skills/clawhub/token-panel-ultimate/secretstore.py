"""
Token Panel — first-party secret store.

Every provider credential this dashboard uses is ITS OWN credential, issued to it by you.
Nothing here reads another application's credential store.

Storage order, best first:
  1. Linux  — libsecret via `secret-tool` (the value is passed on STDIN, never in argv).
  2. macOS  — Keychain via `security`.
  3. Fallback — a 0600 file inside a 0700 directory, WITH A WARNING PRINTED EVERY RUN.

Lookup order when a collector asks for a secret:
  1. This store (keychain, or the warned 0600 fallback file).
  2. The provider's environment variable, for CI and one-shot use.

Off switch: `clear_secret()` removes the secret from BOTH stores and prints the provider's
server-side revoke URL, because deleting a local copy is not revocation.

CLI:
    python3 secretstore.py --status
    python3 secretstore.py --login anthropic     # reads the secret from stdin
    python3 secretstore.py --logout anthropic
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

SERVICE = "token-panel-ultimate"

# Where the fallback lives when the machine has no keychain at all.
FALLBACK_DIR = Path.home() / ".openclaw" / "data" / "token-panel"
FALLBACK_FILE = FALLBACK_DIR / "credentials"

# Each provider: the env var we also accept, and the page where the credential is
# revoked SERVER-SIDE. Deleting the local copy does not revoke anything.
PROVIDERS = {
    "anthropic": {
        "env": "TOKEN_PANEL_ANTHROPIC_TOKEN",
        "also_env": "ANTHROPIC_ADMIN_API_KEY",
        "revoke_url": "https://console.anthropic.com/settings/keys",
        "revoke_note": "delete the API key there to revoke it server-side.",
    },
    "openai": {
        "env": "TOKEN_PANEL_OPENAI_KEY",
        "also_env": "OPENAI_API_KEY",
        "revoke_url": "https://platform.openai.com/api-keys",
        "revoke_note": "delete the API key there to revoke it server-side.",
    },
    "gemini": {
        "env": "TOKEN_PANEL_GEMINI_KEY",
        "also_env": "GEMINI_API_KEY",
        "revoke_url": "https://aistudio.google.com/apikey",
        "revoke_note": "delete the API key there to revoke it server-side.",
    },
    "manus": {
        "env": "TOKEN_PANEL_MANUS_KEY",
        "also_env": "MANUS_API_KEY",
        "revoke_url": "https://manus.im/",
        "revoke_note": "delete the key in your Manus account settings to revoke it server-side.",
    },
}

FALLBACK_WARNING = (
    "WARNING: no OS keychain was found (neither `secret-tool` nor macOS `security`), so this\n"
    "         credential is stored in a plain 0600 file at:\n"
    "           {path}\n"
    "         Any process running as your user can read it. Install libsecret to use the\n"
    "         keychain instead (Debian/Ubuntu: `sudo apt install libsecret-tools`), then\n"
    "         re-run the --login command."
)


def _have(binary: str) -> bool:
    return shutil.which(binary) is not None


def backend() -> str:
    """Which store will be used: 'libsecret', 'macos', or 'file'."""
    if sys.platform == "darwin" and _have("security"):
        return "macos"
    if _have("secret-tool"):
        return "libsecret"
    return "file"


def _warn_fallback() -> None:
    print(FALLBACK_WARNING.format(path=FALLBACK_FILE), file=sys.stderr)


# ---------------------------------------------------------------------------
# Fallback file (0600 inside a 0700 directory)
# ---------------------------------------------------------------------------

def _read_fallback() -> dict:
    if not FALLBACK_FILE.exists():
        return {}
    st = FALLBACK_FILE.stat()
    if st.st_uid != os.getuid():
        raise PermissionError(f"{FALLBACK_FILE} is not owned by you — refusing to read it.")
    if st.st_mode & 0o077:
        raise PermissionError(
            f"{FALLBACK_FILE} is group/world accessible. Run: chmod 600 {FALLBACK_FILE}"
        )
    out = {}
    for line in FALLBACK_FILE.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def _write_fallback(entries: dict) -> None:
    FALLBACK_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(FALLBACK_DIR, 0o700)
    body = "".join(f"{k}={v}\n" for k, v in sorted(entries.items()))
    fd = os.open(str(FALLBACK_FILE), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        f.write(body)
    os.chmod(FALLBACK_FILE, 0o600)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def set_secret(provider: str, value: str) -> str:
    """Store a secret for `provider`. Returns the backend actually used."""
    if provider not in PROVIDERS:
        raise KeyError(f"unknown provider: {provider}")

    kind = backend()
    if kind == "libsecret":
        r = subprocess.run(
            ["secret-tool", "store", f"--label={SERVICE} {provider}",
             "service", SERVICE, "account", provider],
            input=value, text=True,
        )
        if r.returncode == 0:
            return "keychain:libsecret"
    elif kind == "macos":
        # `security` has no stdin path for generic passwords; -w keeps it off the
        # shell history but it is briefly visible in this process's own argv.
        r = subprocess.run(
            ["security", "add-generic-password", "-U", "-s", SERVICE, "-a", provider, "-w", value],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        if r.returncode == 0:
            return "keychain:macos"

    entries = _read_fallback()
    entries[provider] = value
    _write_fallback(entries)
    _warn_fallback()
    return "file"


def get_secret(provider: str) -> tuple[str | None, str | None]:
    """Return (secret, source) for `provider`, or (None, None) if unset.

    Store first, then the provider's environment variables.
    """
    if provider not in PROVIDERS:
        raise KeyError(f"unknown provider: {provider}")

    kind = backend()
    if kind == "libsecret":
        r = subprocess.run(
            ["secret-tool", "lookup", "service", SERVICE, "account", provider],
            capture_output=True, text=True,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip(), "keychain:libsecret"
    elif kind == "macos":
        r = subprocess.run(
            ["security", "find-generic-password", "-s", SERVICE, "-a", provider, "-w"],
            capture_output=True, text=True,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip(), "keychain:macos"

    if FALLBACK_FILE.exists():
        value = _read_fallback().get(provider)
        if value:
            _warn_fallback()
            return value, "file"

    spec = PROVIDERS[provider]
    for env_name in (spec["env"], spec["also_env"]):
        value = os.environ.get(env_name)
        if value:
            return value, f"env:{env_name}"

    return None, None


def clear_secret(provider: str) -> list[str]:
    """The off switch. Remove the secret from BOTH stores and print the revoke URL.

    Returns the list of stores it was actually removed from.
    """
    if provider not in PROVIDERS:
        raise KeyError(f"unknown provider: {provider}")

    cleared = []

    if _have("secret-tool"):
        found = subprocess.run(
            ["secret-tool", "lookup", "service", SERVICE, "account", provider],
            capture_output=True, text=True,
        )
        if found.returncode == 0 and found.stdout.strip():
            r = subprocess.run(
                ["secret-tool", "clear", "service", SERVICE, "account", provider],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            if r.returncode == 0:
                cleared.append("keychain:libsecret")

    if sys.platform == "darwin" and _have("security"):
        r = subprocess.run(
            ["security", "delete-generic-password", "-s", SERVICE, "-a", provider],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        if r.returncode == 0:
            cleared.append("keychain:macos")

    entries = _read_fallback()
    if provider in entries:
        del entries[provider]
        if entries:
            _write_fallback(entries)
        else:
            FALLBACK_FILE.unlink()
        cleared.append(f"file:{FALLBACK_FILE}")

    spec = PROVIDERS[provider]
    print(f"Local copies removed: {', '.join(cleared) if cleared else 'none were stored'}")
    for env_name in (spec["env"], spec["also_env"]):
        if os.environ.get(env_name):
            print(f"NOTE: {env_name} is still set in this environment — unset it too.")
    print(
        f"\nThis only deleted local copies. To REVOKE the credential server-side, open:\n"
        f"  {spec['revoke_url']}\n"
        f"  ({spec['revoke_note']})"
    )
    return cleared


def status() -> None:
    print(f"backend: {backend()}")
    if backend() == "file":
        print(f"         (no OS keychain; fallback file is {FALLBACK_FILE})")
    for provider in sorted(PROVIDERS):
        value, source = get_secret(provider)
        print(f"  {provider:<10} {'set   via ' + source if value else 'not set'}")


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Token Panel credential store")
    ap.add_argument("--status", action="store_true", help="Show which providers have a stored credential")
    ap.add_argument("--login", metavar="PROVIDER", help="Store a credential (read from stdin)")
    ap.add_argument("--logout", metavar="PROVIDER", help="Remove a credential from every local store")
    args = ap.parse_args()

    if args.login:
        if args.login not in PROVIDERS:
            print(f"Unknown provider: {args.login}. Known: {', '.join(sorted(PROVIDERS))}", file=sys.stderr)
            return 1
        if sys.stdin.isatty():
            print(f"Paste the {args.login} credential, then press Ctrl-D:", file=sys.stderr)
        value = sys.stdin.read().strip()
        if not value:
            print("Nothing read from stdin; aborted.", file=sys.stderr)
            return 1
        where = set_secret(args.login, value)
        print(f"Stored {args.login} credential in: {where}")
        return 0

    if args.logout:
        if args.logout not in PROVIDERS:
            print(f"Unknown provider: {args.logout}. Known: {', '.join(sorted(PROVIDERS))}", file=sys.stderr)
            return 1
        clear_secret(args.logout)
        return 0

    status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
