"""Dispatch one requested stage to its unchanged bundled operation entry point."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage', required=True, choices=('upstream', 'downstream'))
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    entry = Path(__file__).resolve().parents[1] / 'operations' / args.stage / 'scripts/run.py'
    command = [sys.executable, '-I', '-S', '-B', str(entry), '--input', str(args.input.resolve())]
    if args.output_dir is not None:
        command.extend(['--output-dir', str(args.output_dir.resolve())])
    result = subprocess.run(command)
    raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
