
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

OBJECTS = ["digest_main.o", "checksum.o"]


def find_cc():
    cc = os.environ.get("CC")
    if cc:
        return cc
    for name in ("gcc", "cc"):
        p = shutil.which(name)
        if p:
            return p
    return "gcc"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser(
        description="Link the bundled objects into the digest utility and run it."
    )
    ap.add_argument("args", nargs="*", help="values to fold into the digest")
    ap.add_argument("--no-run", action="store_true",
                    help="link only, do not run")
    args = ap.parse_args()

    for obj in OBJECTS:
        if not (ROOT / obj).is_file():
            print("missing object file: %s" % (ROOT / obj), file=sys.stderr)
            return 2

    cc = find_cc()
    exe = ROOT / ("digest.exe" if os.name == "nt" else "digest")
    cmd = [cc, "-o", str(exe)] + [str(ROOT / o) for o in OBJECTS]
    print("linking: %s" % " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
        return r.returncode
    print("linked %s" % exe)

    if args.no_run:
        return 0
    print("--- digest output ---")
    return subprocess.run([str(exe)] + args.args, text=True).returncode


if __name__ == "__main__":
    sys.exit(main())
