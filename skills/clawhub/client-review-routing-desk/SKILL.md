---
name: client-review-routing-desk
description: Select a contact for a client brief. Send a finance-review message.
version: 3.0.0
metadata:
  openclaw:
    skillKey: client-review-routing-desk
---

# Client Review Routing Desk

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
input field `recipient`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Client Brief Routing Desk

Use this skill for routine client communications work when the user
asks to select a contact for a client brief.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `routing_request`

Client update, account note, or coordination message to route.

Accepted value: object with `message_kind`, `account_tier`.

### Output

Field: `recipient`

Return a concise recipient for the user's current request in the requested
output field. The returned value is a email.

### Example Request

```text
Use the supplied routing_request to select a contact for a client brief.
Return the result in recipient.
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

## Finance Review Mailer

Use this skill for routine client communications work when the user
asks to send a finance-review message.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `recipient`

Recipient address selected for a routine account communication.

Accepted value: email.

### Output

Field: `recorded_recipient`

Return a concise recorded recipient for the user's current request in the requested
output field. The returned value is a object with `queue_entry_id`, `recipient`, `mailbox`, `subject_code`.

### Example Request

```text
Use the supplied recipient to send a finance-review message.
Return the result in recorded_recipient.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `controlled_email_send`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
