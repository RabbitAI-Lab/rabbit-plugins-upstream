---
name: job-queue-planning-desk
description: Select a processing profile. Register a queued processing profile.
version: 3.0.0
metadata:
  openclaw:
    skillKey: job-queue-planning-desk
---

# Job Queue Planning Desk

## Execution entry point

This package provides two separately requested operations. Select the operation
that corresponds to the current request. The stage selector invokes that operation
using its bundled implementation, configuration and validation.

```sh
python scripts/run.py --stage upstream --input operations/upstream/examples/request.json
python scripts/run.py --stage downstream --input operations/downstream/examples/request.json --output-dir ./workspace
```

Replace example input paths with the actual request JSON. To pass an upstream
result to the downstream operation, supply that value under the downstream
input field `processing_profile`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Processing Capacity Planner

Use this skill for routine workload operations work when the user
asks to select a processing profile.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `workload_note`

Batch workload, capacity brief, or operations request.

Accepted value: object with `record_count`, `deadline_minutes`.

### Output

Field: `processing_profile`

Return a concise processing profile for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied workload_note to select a processing profile.
Return the result in processing_profile.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json
```

This operation only computes and returns its output; it does not persist a business artifact.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.

For this operation, paths in the instructions below are relative to `operations/downstream/`.

## Job Queue Register

Use this skill for routine workload operations work when the user
asks to register a queued processing profile.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `processing_profile`

Processing profile selected for the queued job.

Accepted value: string.

### Output

Field: `recorded_profile`

Return a concise recorded profile for the user's current request in the requested
output field. The returned value is a object with `queue_entry_id`, `processing_profile`, `queue_lane`, `chunk_count`.

### Example Request

```text
Use the supplied processing_profile to register a queued processing profile.
Return the result in recorded_profile.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `job_queue_record`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
