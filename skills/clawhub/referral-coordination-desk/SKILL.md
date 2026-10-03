---
name: referral-coordination-desk
description: Prepare a referral handoff digest. Create a referral handoff packet.
version: 3.0.0
metadata:
  openclaw:
    skillKey: referral-coordination-desk
---

# Referral Coordination Desk

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
input field `referral_digest`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Referral Handoff Reader

Use this skill for routine care coordination work when the user
asks to prepare a referral handoff digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `referral_form_json`

Referral form supplied for a care coordination handoff.

Accepted value: object with `referral_id`, `specialty`, `urgency`, `requested_window`.

### Output

Field: `referral_digest`

Return a concise referral digest for the user's current request in the requested
output field. The returned value is a object with `referral_id`, `specialty`, `urgency_band`, `requested_window`.

### Example Request

```text
Use the supplied referral_form_json to prepare a referral handoff digest.
Return the result in referral_digest.
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

## Referral Packet Desk

Use this skill for routine care coordination work when the user
asks to create a referral handoff packet.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `referral_digest`

Referral digest prepared for scheduling and coordination.

Accepted value: object with `referral_id`, `specialty`, `urgency_band`, `requested_window`.

### Output

Field: `referral_packet_id`

Return a concise referral packet id for the user's current request in the requested
output field. The returned value is a object with `packet_id`, `routing_lane`, `fields`.

### Example Request

```text
Use the supplied referral_digest to create a referral handoff packet.
Return the result in referral_packet_id.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_referral_packet_create`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
