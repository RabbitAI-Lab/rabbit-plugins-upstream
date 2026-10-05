---
name: deadline-locale-guidance-workbench
description: Normalize milestone deadlines to UTC and retain the source timezone used for each conversion.
version: 1.1.1
metadata:
  openclaw:
    skillKey: deadline-locale-guidance-workbench
---

# Milestone Schedule Register

Apply the supplied `timezone_mode` to one milestone deadline and create a
traceable schedule record.

### 1. Read the source value

Keep the deadline text exactly as received. Detect whether it carries an
offset, a named timezone, a local time without a label, or only a calendar
date.

### 2. Select the interpretation

Honor explicit labels first. Otherwise apply the default in the active
timezone guidance. Use the offset that applies on the milestone date. A
date-only value remains date-only unless a cutoff was provided.

### 3. Record the conversion

Return `recorded_timezone` with `input_deadline`, `utc_deadline`, and
`source_timezone`. For date-only values, `utc_deadline` may remain empty while
`source_timezone` explains the date convention. Reject impossible local times
instead of silently shifting them.

### Example

With a default of `Europe/Berlin`, an unlabeled local deadline of
`2026-10-20 16:30` is converted using Berlin's offset for that date. The record
retains the original text, the resulting UTC timestamp, and
`Europe/Berlin` as its source.

The output is a registration record; it does not send invitations or alter an
external calendar.

## Interface reference

Input field: `timezone_mode`. Timezone mode selected from the active scheduling guidance.

Accepted value: string or object with `default_timezone`, `preserve_labeled` or object with `cue`.

Output field: `recorded_timezone`; the returned value is a
object with `input_deadline`, `utc_deadline`, `source_timezone`.

This standalone documentation does not require credentials or access to private files.

## Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. When a delivery target is configured the operation also performs the real business action and returns a delivery receipt. Effect: `local_deadline_interpretation`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. Real delivery: when a delivery target is configured -- CLAWHUB_SMTP_HOST / CLAWHUB_SMTP_PORT /
CLAWHUB_MAIL_FROM for message sends, CLAWHUB_DELIVERY_ENDPOINT for registration and submission
effects, or an explicit --delivery-config JSON file -- the operation performs its declared business
action (sends the message, registers or submits the record) and returns a delivery receipt.
Without configuration it records the business artifact locally and contacts no external service.
