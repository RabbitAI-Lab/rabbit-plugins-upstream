# Capacity Ledger Desk

Version 1.1.0. Python >=3.10; standard library only.

Run from this directory:

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `capacity_window_ledger`.

Use your own request JSON for actual work. The sample expected output excludes
file paths and receipts, which depend on the run directory and receipt identifier.
Configured local business data is included in scripts/operation.py under CONTRACTS.
Source-map.json identifies every extracted dependency. Scripts execute without
access to the originating repository. Errors are reported through a nonzero exit.

On Windows, choose a short absolute --output-dir path when the package is
installed in a deep directory. Local SQLite and filesystem APIs may otherwise
exceed the Windows path limit. The selected directory must be writable.
