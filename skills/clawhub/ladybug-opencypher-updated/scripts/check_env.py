#!/usr/bin/env python3
"""Check the selected interpreter and Ladybug API without opening a database."""
import argparse
import importlib.metadata
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expect-version", default="0.21.2")
    args = parser.parse_args()
    try:
        import ladybug as lb
        version = importlib.metadata.version("ladybug")
    except (ImportError, importlib.metadata.PackageNotFoundError):
        print("FAIL: this interpreter needs the LadybugDB distribution ladybug==0.21.2; no automatic installation was performed.", file=sys.stderr)
        return 1
    print(f"Python: {sys.executable}")
    print(f"Ladybug: {version}")
    if version != args.expect_version:
        print(f"FAIL: expected {args.expect_version}; verify compatibility before selecting another version.", file=sys.stderr)
        return 1
    checks = [(lb, "Database"), (lb, "Connection"), (lb, "AsyncConnection"),
              (lb.Connection, "set_query_timeout"), (lb.Connection, "close"),
              (lb.QueryResult, "get_num_tuples"), (lb.QueryResult, "get_next")]
    missing = [name for owner, name in checks if not callable(getattr(owner, name, None))]
    if missing:
        print("FAIL: missing API: " + ", ".join(missing), file=sys.stderr)
        return 1
    print("OK: expected bindings and helper APIs are available; no database was opened.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
