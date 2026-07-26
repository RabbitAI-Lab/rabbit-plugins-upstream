"""
desktop-control daemon — entry point.
Call once to start the background named-pipe server.
"""
import os
import sys
import threading

# Ensure the skill root is importable
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if SKILL_DIR not in sys.path:
    sys.path.insert(0, SKILL_DIR)

from daemon.utils import lifecycle, sendinput
from daemon.utils.monitors import refresh_monitors, get_monitor_count
from daemon.server import NamedPipeServer


PIPE_INFO_FILE = os.path.join(os.environ.get("TEMP", os.path.expanduser("~")),
                               "oc_desktop_pipe.txt")


def main():
    # 1. DPI awareness (must run early)
    sendinput.enable_dpi_awareness()

    # 2. Ensure single instance
    lifecycle.try_acquire_or_exit()

    # 3. Cache monitor layout (single-shot at startup)
    refresh_monitors()

    # 4. Start named-pipe server
    server = NamedPipeServer()

    def shutdown():
        lifecycle.clean_pid_file()
        if os.path.exists(PIPE_INFO_FILE):
            try:
                os.remove(PIPE_INFO_FILE)
            except OSError:
                pass
        # Release any stuck inputs before stopping everything
        try:
            from daemon.utils.release_guard import shutdown as rg_shutdown
            rg_shutdown()
        except Exception:
            pass
        server.stop()

    lifecycle.register_shutdown_hook(shutdown)

    server.start()
    pipe_name = server.pipe_name

    # 5. Write pipe name and PID for the client to discover
    lifecycle.write_pid_file()
    with open(PIPE_INFO_FILE, "w") as f:
        f.write(pipe_name)

    print(f"desktop-control daemon ready on {pipe_name} [pid {os.getpid()}]")
    print(f"  Monitors: {get_monitor_count()} detected")

    # 6. Block forever (or until shutdown)
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        shutdown()


if __name__ == "__main__":
    main()
