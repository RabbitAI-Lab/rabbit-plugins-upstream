---
name: service-capacity-window-workbench
description: Record a capacity-window entry.
version: 1.1.0
metadata:
  openclaw:
    skillKey: service-capacity-window-workbench
---

# Capacity Ledger Desk

Use this skill for routine service capacity planning work when the user
asks to record a capacity-window entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `capacity_window`

Timezone-aware service window selected for the capacity ledger.

Accepted value: date-time.

## Output

Field: `capacity_ledger_entry`

Return a concise capacity ledger entry for the user's current request in the requested
output field. The returned value is a object with `capacity_entry_id`, `start_at`, `end_at`, `duration_minutes`, `total_slots`, `requested_slots`, `reserved_slots`, `available_slots`, `capacity_status`, `overlap_status`.

## Example Request

```text
Use the supplied capacity_window to record a capacity-window entry.
Return the result in capacity_ledger_entry.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `capacity_window_ledger`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
