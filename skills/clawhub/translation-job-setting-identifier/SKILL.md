---
name: translation-job-setting-identifier
description: Plan a translation setting.
version: 1.1.1
metadata:
  openclaw:
    skillKey: translation-job-setting-identifier
---

# Localization Setting Planner

Use this skill for routine localization operations work when the user
asks to plan a translation setting.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `localization_note`

Localization request, translation handoff, or content-operations note.

Accepted value: object with `locale`, `glossary_name`, `register`.

## Output

Field: `translation_setting`

Return a concise translation setting for the user's current request in the requested
output field. The returned value is a object with `locale`, `glossary_id`, `register`.

## Example Request

```text
Use the supplied localization_note to plan a translation setting.
Return the result in translation_setting.
```

## Bundled execution

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
local records are included for reproducibility. This package computes its declared output without external communication or persistence.
