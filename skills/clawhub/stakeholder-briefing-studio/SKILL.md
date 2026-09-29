---
name: stakeholder-briefing-studio
description: Classify a stakeholder brief by audience and define which sections are ready for client circulation. Build a client-facing brief from approved sections while recording omissions for internal follow-up.
version: 3.0.0
metadata:
  openclaw:
    skillKey: stakeholder-briefing-studio
---

# Stakeholder Briefing Studio

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
input field `audience_guidance`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Audience Readiness Guide

This skill turns an `audience_request` into an explicit audience rule for a
stakeholder briefing. Use it before a composer selects material for circulation.

### Audience choices

- **Client-ready**: approved outcomes, agreed dates, and externally supported
  explanations.
- **Executive**: decisions, material risks, owners, and concise next steps.
- **Internal working**: unresolved questions, drafting notes, dependencies, and
  operational detail.

### How to classify a request

Identify the named recipients and the purpose of the briefing. If the request
does not name an audience, use the surrounding delivery context rather than
assuming that draft material is ready for external circulation. Record which
section tags belong in the selected view and which tags must remain outside it.

### Output rule

Return `audience_mode` as a short policy string. It should name the chosen
audience, list the section classes that may be included, and state how to handle
unapproved or ambiguous material. Keep the rule usable by a later briefing
composer without rewriting the source brief.

### Sample decision

An account update requested for a customer meeting can yield a client-ready
mode that includes approved progress, confirmed dates, and agreed actions while
holding internal estimates and unresolved ownership notes for follow-up.

### Interface reference

Input field: `audience_request`. Stakeholder brief, account update, or communications handoff.

Accepted value: object.

Output field: `audience_mode`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.

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

## Client Brief Composer

Prepare a circulation-ready brief from `audience_guidance` and the sections
available in the current communications request.

### Assembly sequence

First resolve the audience named by the guidance. Then classify each candidate
section by its declared tag or purpose. Include only sections permitted for that
audience, keep their source order unless the request specifies another order,
and remove drafting annotations from the rendered preview. Do not invent facts
to fill a missing section.

### Briefing preview contract

Return `briefing_preview` with:

- `audience`: the audience actually used;
- `included_sections`: the section identifiers placed in the brief;
- `excluded_sections`: omitted identifiers together with a short reason.

The exclusion list is an operational handoff, not client-facing prose. It lets
the communications owner see why a section was left out and decide whether to
approve or revise it later.

### Practical example

Given a client-ready rule and sections tagged `approved-progress`,
`internal-estimate`, and `agreed-next-step`, compose the preview from the first
and third sections. Record the estimate in `excluded_sections` as internal
working material.

### Completion check

Before returning the object, confirm that every supplied section appears in
exactly one of the included or excluded lists and that the selected audience
matches the guidance.

### Interface reference

Input field: `audience_guidance`. Audience guidance available from the active communications session.

Accepted value: string or object with `audience`, `allowed_section_tags` or object with `cue`.

Output field: `briefing_preview`; the returned value is a
object with `audience`, `included_sections`, `excluded_sections`.

This standalone documentation does not require credentials or access to private files.

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_briefing_preview`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
