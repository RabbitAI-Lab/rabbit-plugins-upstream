"""home_music — Python interface for the home-music whole-house audio skill.

This is a thin wrapper around the macOS shell script (home-music.sh) so that
automations (like the daily financial report) can start and — importantly —
STOP music programmatically.

Design notes
------------
- Single source of truth: actual speaker/Spotify control lives in home-music.sh.
  This module just shells out to it, so behavior never drifts between the CLI
  and the Python API.
- Safe to import/run anywhere: set HOME_MUSIC_DRY_RUN=1 (or pass dry_run=True)
  to print the intended command without invoking macOS-only tooling. This lets
  the call chain be tested on non-macOS hosts (CI/Linux) without speakers.
- Never fatal: a failure to control music must never crash the surrounding
  automation. Callers can opt into raising via raise_on_error=True.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

__all__ = ["play_chill_mode", "play_focus_mode", "stop_music", "run_scene"]


def _script_path() -> str:
    """Locate home-music.sh.

    Order: HOME_MUSIC_SCRIPT env override -> sibling skills/ dirs -> PATH.
    """
    override = os.environ.get("HOME_MUSIC_SCRIPT")
    if override:
        return override

    here = Path(__file__).resolve().parent
    candidates = [
        here / "home-music.sh",                          # co-located copy
        here.parent / "skills" / "home-music" / "home-music.sh",
        here.parent / "home-music" / "home-music.sh",
    ]
    for c in candidates:
        if c.exists():
            return str(c)

    on_path = shutil.which("home-music")
    if on_path:
        return on_path

    # Fall back to the documented install location; let the caller's error
    # handling deal with a missing file rather than guessing silently.
    return str(candidates[0])


def _is_dry_run(explicit: bool | None) -> bool:
    if explicit is not None:
        return explicit
    return os.environ.get("HOME_MUSIC_DRY_RUN", "").strip().lower() in {"1", "true", "yes", "on"}


def run_scene(scene: str, *args: str, dry_run: bool | None = None,
              raise_on_error: bool = False) -> int:
    """Run a home-music scene via the shell script.

    Returns the script's exit code (0 = success). In dry-run mode, prints the
    command and returns 0 without executing it.
    """
    cmd = [_script_path(), scene, *[str(a) for a in args]]

    if _is_dry_run(dry_run):
        print(f"[home_music][DRY_RUN] would run: {' '.join(cmd)}")
        return 0

    try:
        result = subprocess.run(cmd, check=False)
        if result.returncode != 0:
            print(f"[home_music] scene '{scene}' exited with code {result.returncode}")
            if raise_on_error:
                raise RuntimeError(f"home-music scene '{scene}' failed (exit {result.returncode})")
        return result.returncode
    except FileNotFoundError as exc:
        print(f"[home_music] could not run home-music script: {exc}")
        if raise_on_error:
            raise
        return 127


def play_chill_mode(volume: int = 30, *, dry_run: bool | None = None,
                    raise_on_error: bool = False) -> int:
    """Start the chill lounge scene (low-key background music)."""
    # Chill scene currently uses a fixed volume in the script; volume is passed
    # through for forward-compat and logging clarity.
    print(f"[home_music] play_chill_mode(volume={volume})")
    return run_scene("chill", dry_run=dry_run, raise_on_error=raise_on_error)


def play_focus_mode(volume: int = 30, *, dry_run: bool | None = None,
                    raise_on_error: bool = False) -> int:
    """Start the deep-focus work-session scene at the given volume percent."""
    print(f"[home_music] play_focus_mode(volume={volume})")
    return run_scene("focus", int(volume), dry_run=dry_run, raise_on_error=raise_on_error)


def stop_music(*, dry_run: bool | None = None, raise_on_error: bool = False) -> int:
    """Stop all music: pause Spotify and disconnect every speaker.

    This is the function that was previously missing — automations should call
    it when their work is done so music does not keep playing indefinitely.
    """
    print("[home_music] stop_music()")
    return run_scene("off", dry_run=dry_run, raise_on_error=raise_on_error)
