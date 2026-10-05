---
name: delivery-document-desk
description: Determine a signature requirement. Compose a delivery signature section.
version: 3.0.0
metadata:
  openclaw:
    skillKey: delivery-document-desk
---

# Delivery Document Desk

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
input field `requires_signature`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Delivery Requirement Advisor

Use this skill for routine delivery operations work when the user
asks to determine a signature requirement.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `delivery_request`

Package class and service level for a delivery handoff.

Accepted value: object with `package_class`, `service_level`.

### Output

Field: `requires_signature`

Return a concise requires signature for the user's current request in the requested
output field. The returned value is a boolean.

### Example Request

```text
Use the supplied delivery_request to determine a signature requirement.
Return the result in requires_signature.
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

## Delivery Document Composer

Use this skill for routine delivery operations work when the user
asks to compose a delivery signature section.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `requires_signature`

Recipient-signature requirement selected for the delivery handoff document.

Accepted value: boolean.

### Output

Field: `delivery_document_section`

Return a concise delivery document section for the user's current request in the requested
output field. The returned value is a object with `section_id`, `requires_signature`, `signature_section`, `document_count`.

### Example Request

```text
Use the supplied requires_signature to compose a delivery signature section.
Return the result in delivery_document_section.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `delivery_documentation_record`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
