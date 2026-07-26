#!/usr/bin/env python3
"""
chameleon_control.py - Drive the interactive Chameleon Ultra CLI
(chameleon_cli_main) in a non-interactive, scriptable way.

The official chameleon_cli_main is an interactive REPL built on
prompt_toolkit, so it cannot be driven by simply piping stdin on Windows
(prompt_toolkit needs a real console). This script wraps the executable in a
pseudo-terminal (winpty on Windows, pty on POSIX) so it can be controlled
programmatically and its output captured.

Usage:
  python chameleon_control.py --set-exe "C:\\path\\to\\chameleon_cli_main.exe"
  python chameleon_control.py --show-config
  python chameleon_control.py "hw connect" "hf 14a scan"
  python chameleon_control.py --file commands.txt
  python chameleon_control.py --no-connect "hw version"

Config (exe path) is persisted in config.json next to this script.
"""
import os
import sys
import json
import time
import argparse
import subprocess
import threading
import re

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SKILL_DIR, "config.json")

# ANSI escape sequence stripper
_ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]")
# Chameleon prompt looks like:  [USB] chameleon -->   or  [Offline] chameleon -->
_PROMPT_RE = re.compile(r"\[[^\]]*\]\s*chameleon\s*-->\s*")


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {"exe_path": ""}
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cfg = json.load(f)
        if not isinstance(cfg, dict):
            cfg = {}
        cfg.setdefault("exe_path", "")
        return cfg
    except Exception:
        return {"exe_path": ""}


def save_config(cfg):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)


def handle_config(args):
    cfg = load_config()
    if args.set_exe:
        exe = args.set_exe.strip().strip('"').strip("'")
        if not exe:
            print("[!] Empty executable path provided.", file=sys.stderr)
            sys.exit(1)
        if not os.path.exists(exe):
            print(f"[!] File not found: {exe}", file=sys.stderr)
            print("    The path will still be saved, but verify it is correct.", file=sys.stderr)
        cfg["exe_path"] = exe
        save_config(cfg)
        print(f"[OK] Saved executable path:")
        print(f"     {exe}")
        return
    # --show-config (default when no commands and no set_exe)
    print("Current configuration:")
    print(f"  exe_path : {cfg.get('exe_path') or '(not set)'}")
    if not cfg.get("exe_path"):
        print("  -> Run: python chameleon_control.py --set-exe \"C:\\\\path\\\\to\\\\chameleon_cli_main.exe\"")


def ensure_deps():
    """Ensure the PTY backend is available. On Windows, winpty may be bootstrapped
    into a local venv and this process re-executed with that interpreter."""
    if os.name == "nt":
        try:
            import winpty  # noqa: F401
            return
        except ImportError:
            bootstrap_winpty()
    # POSIX: pty is part of the standard library.


def bootstrap_winpty():
    venv_dir = os.path.join(SKILL_DIR, ".venv")
    if os.name == "nt":
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(venv_dir, "bin", "python")
    if not os.path.exists(venv_python):
        print("[*] First run: creating local venv and installing pywinpty (one-time)...",
              file=sys.stderr)
        try:
            subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
            subprocess.run([venv_python, "-m", "pip", "install", "-q", "--upgrade", "pip"],
                           check=True)
            subprocess.run([venv_python, "-m", "pip", "install", "-q", "pywinpty"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"[!] Failed to install pywinpty: {e}", file=sys.stderr)
            print("    Make sure network access is available, then retry.", file=sys.stderr)
            sys.exit(1)
    # Re-run with the venv interpreter so winpty can be imported.
    # NOTE: use subprocess.run (not os.execv) so the child's stdout/stderr
    # are inherited and captured by the calling shell; on some Windows
    # setups os.execv silently drops the child's output.
    subprocess.run([venv_python, __file__, *sys.argv[1:]], check=True)
    sys.exit(0)


def read_commands_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f]
    return [ln for ln in lines if ln and not ln.startswith("#")]


def respond_to_queries(data, pty_obj):
    """prompt_toolkit probes terminal capabilities at startup by emitting
    Device-Attributes / cursor-position queries and waits for a response
    before it will draw the prompt. A raw winpty PTY does not answer these,
    so the REPL hangs with no visible output. Answer the queries here.

    NOTE: winpty echoes our injected responses back into the output stream,
    but they are CSI sequences (ending in 'c' / 'R') which the ANSI stripper
    in clean_output() removes, so they never reach the user. The OSC window
    title query (\\x1b[1t) is intentionally NOT answered to avoid OSC echo
    pollution; the REPL proceeds fine without it.
    """
    try:
        if "\x1b[c" in data:        # Primary Device Attributes
            pty_obj.write("\x1b[?6c")
        if "\x1b[>c" in data:       # Terminal version string
            pty_obj.write("\x1b[>0;0;0c")
        if "\x1b[6n" in data:       # Cursor position report request (DSR)
            pty_obj.write("\x1b[1;1R")
    except Exception:
        pass


def reader_thread(pty_obj, out_list, stop_event):
    """Continuously read from the pty until EOF."""
    while not stop_event.is_set():
        try:
            data = pty_obj.read(65536)
        except EOFError:
            break
        except Exception:
            break
        if data == "" or data is None:
            # On some backends '' means EOF.
            if not pty_obj.isalive():
                break
            continue
        out_list.append(data)
        # Answer terminal-capability queries so prompt_toolkit renders.
        respond_to_queries(data, pty_obj)


def clean_output(raw, commands, keep_raw):
    if keep_raw:
        return raw
    text = _ANSI_RE.sub("", raw)
    # Remove the echoed input that follows each prompt (console line-echo).
    for cmd in commands:
        # Keep the prompt, drop the echoed command that trails it.
        text = re.sub(_PROMPT_RE.pattern + re.escape(cmd), lambda m: m.group(0).rsplit(cmd, 1)[0], text)
        # Also drop a standalone echoed command line if present.
        text = re.sub(r"(?m)^" + re.escape(cmd) + r"\s*$", "", text)
    # Collapse excessive blank lines.
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def run_windows(exe_path, commands, max_timeout, keep_raw):
    import winpty
    cmd = exe_path if isinstance(exe_path, (list, tuple)) else [exe_path]
    p = winpty.PtyProcess.spawn(cmd)
    stop = threading.Event()
    out_list = []
    t = threading.Thread(target=reader_thread, args=(p, out_list, stop), daemon=True)
    t.start()
    # Give the REPL a moment to print its banner / prompt.
    time.sleep(0.8)
    for cmd in commands:
        # IMPORTANT: prompt_toolkit accepts LF ('\n') as the "execute" key.
        # CR ('\r') is interpreted as a completion/insertion and leaves the
        # command un-executed, so always terminate with '\n'.
        p.write(cmd + "\n")
        time.sleep(0.4)
    # Wait for the session to finish (process exits after our final 'exit').
    t.join(timeout=max_timeout)
    if t.is_alive():
        # Timed out (e.g. a command is waiting for a tag). Interrupt and bail.
        try:
            p.write("\x03")
            time.sleep(0.3)
            p.write("exit\n")
        except Exception:
            pass
        t.join(timeout=5)
        stop.set()
        try:
            p.terminate()
        except Exception:
            pass
    else:
        stop.set()
    raw = "".join(out_list)
    return clean_output(raw, commands, keep_raw)


def run_posix(exe_path, commands, max_timeout, keep_raw):
    import pty
    import select

    class _PosixWriter:
        """Adapter so respond_to_queries() can write back to the pty master."""
        def __init__(self, proc, master_fd):
            self.proc = proc
            self.master_fd = master_fd

        def write(self, s):
            try:
                os.write(self.master_fd, s.encode("utf-8", "replace"))
            except Exception:
                pass

    master, slave = pty.openpty()
    proc = subprocess.Popen([exe_path], stdin=slave, stdout=slave, stderr=slave,
                            close_fds=True)
    os.close(slave)
    stop = threading.Event()
    out_list = []

    def reader():
        while not stop.is_set():
            try:
                r, _, _ = select.select([master], [], [], 0.2)
                if not r:
                    if proc.poll() is not None:
                        break
                    continue
                data = os.read(master, 65536)
                if not data:
                    break
                text = data.decode(errors="replace")
                out_list.append(text)
                # Answer terminal-capability queries so prompt_toolkit renders.
                respond_to_queries(text, _PosixWriter(proc, master))
            except (OSError, EOFError):
                break

    t = threading.Thread(target=reader, daemon=True)
    t.start()
    time.sleep(0.5)
    for cmd in commands:
        os.write(master, (cmd + "\r\n").encode())
        time.sleep(0.4)
    t.join(timeout=max_timeout)
    if t.is_alive():
        try:
            os.write(master, b"\x03")
            time.sleep(0.3)
            os.write(master, b"exit\r\n")
        except Exception:
            pass
        t.join(timeout=5)
        stop.set()
        try:
            proc.terminate()
        except Exception:
            pass
    else:
        stop.set()
    raw = "".join(out_list)
    return clean_output(raw, commands, keep_raw)


def build_commands(args):
    cmds = []
    if args.file:
        cmds.extend(read_commands_from_file(args.file))
    cmds.extend(args.commands)
    # Auto-connect unless disabled or already present.
    if not args.no_connect:
        if not cmds or cmds[0].strip().lower() not in ("hw connect", "hw disconnect"):
            cmds.insert(0, "hw connect")
    # Always exit cleanly at the end so the process terminates.
    cmds.append("exit")
    return cmds


def main():
    parser = argparse.ArgumentParser(
        description="Control the Chameleon Ultra CLI (chameleon_cli_main) non-interactively.")
    parser.add_argument("commands", nargs="*", help="Chameleon CLI commands to run, in order.")
    parser.add_argument("--set-exe", metavar="PATH",
                        help="Save the path to chameleon_cli_main(.exe) and exit.")
    parser.add_argument("--show-config", action="store_true",
                        help="Print the current configuration and exit.")
    parser.add_argument("--file", metavar="FILE",
                        help="Read commands from a file (one per line, # for comments).")
    parser.add_argument("--no-connect", action="store_true",
                        help="Do not auto-prepend 'hw connect'.")
    parser.add_argument("--timeout", type=float, default=120.0,
                        help="Max seconds to wait for the whole session (default 120).")
    parser.add_argument("--raw", action="store_true",
                        help="Do not strip ANSI codes / echoed input.")
    args = parser.parse_args()

    # Config-only operations do not require the PTY backend.
    if args.set_exe:
        handle_config(args)
        return
    if args.show_config or (not args.commands and not args.file):
        handle_config(args)
        return

    ensure_deps()

    cfg = load_config()
    exe_path = cfg.get("exe_path", "")
    if not exe_path:
        print("[!] chameleon_cli_main executable path is not configured.", file=sys.stderr)
        print("    Run: python chameleon_control.py --set-exe \"C:\\\\path\\\\to\\\\chameleon_cli_main.exe\"",
              file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(exe_path):
        print(f"[!] Executable not found at configured path: {exe_path}", file=sys.stderr)
        print("    Re-run --set-exe with the correct path.", file=sys.stderr)
        sys.exit(1)

    commands = build_commands(args)
    try:
        if os.name == "nt":
            result = run_windows(exe_path, commands, args.timeout, args.raw)
        else:
            result = run_posix(exe_path, commands, args.timeout, args.raw)
    except KeyboardInterrupt:
        print("[!] Interrupted by user.", file=sys.stderr)
        sys.exit(1)
    print(result)


if __name__ == "__main__":
    main()
