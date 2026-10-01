---
name: translation-job-setting-workbench
description: Build a translation job entry.
version: 1.1.0
metadata:
  openclaw:
    skillKey: translation-job-setting-workbench
---

# Translation Job Desk

Use this skill for routine localization operations work when the user
asks to build a translation job entry.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `translation_setting`

Translation setting selected for the localization job.

Accepted value: object with `locale`, `glossary_id`, `register`.

## Output

Field: `recorded_translation_setting`

Return a concise recorded translation setting for the user's current request in the requested
output field. The returned value is a object with `job_code`, `locale`, `glossary_id`, `register`, `segment_limit`.

## Example Request

```text
Use the supplied translation_setting to build a translation job entry.
Return the result in recorded_translation_setting.
```

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `translation_job_entry`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
