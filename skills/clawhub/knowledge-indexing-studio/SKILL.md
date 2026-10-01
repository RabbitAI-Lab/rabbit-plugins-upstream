---
name: knowledge-indexing-studio
description: Segment a knowledge note for indexing. Update a section and backlink index.
version: 3.0.0
metadata:
  openclaw:
    skillKey: knowledge-indexing-studio
---

# Knowledge Indexing Studio

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
input field `segmented_note`. The caller controls this handoff.
Upstream computes a result; downstream also persists its documented local artifact.
Return the actual output and effect receipt. Require Python 3.10+ and a writable
output directory for downstream. All dependencies are from the standard library.

For this operation, paths in the instructions below are relative to `operations/upstream/`.

## Knowledge Note Segmenter

Use this skill for routine knowledge operations work when the user
asks to segment a knowledge note for indexing.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `knowledge_note`

Knowledge note with a reference, headings, tags, and related links.

Accepted value: string.

### Output

Field: `segmented_note`

Return a concise segmented note for the user's current request in the requested
output field. The returned value is a object with `reference`, `heading`, `tags`, `links`, `content_digest`, `sections`.

### Example Request

```text
Use the supplied knowledge_note to segment a knowledge note for indexing.
Return the result in segmented_note.
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

## Knowledge Index Curator

Use this skill for routine knowledge operations work when the user
asks to update a section and backlink index.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `segmented_note`

Referenced note sections prepared for the shared knowledge index.

Accepted value: object with `reference`, `heading`, `tags`, `links`, `content_digest`, `sections`.

### Output

Field: `index_update`

Return a concise index update for the user's current request in the requested
output field. The returned value is a object with `index_id`, `reference`, `heading`, `content_digest`, `indexed_sections`, `backlinks`, `dedup_status`, `duplicates_removed`.

### Example Request

```text
Use the supplied segmented_note to update a section and backlink index.
Return the result in index_update.
```

### Bundled execution

Use Python 3.10 or newer to run this operation from the installed package directory.
Save the actual request as JSON containing the declared input field and pass its path
with --input. The bundled example demonstrates the input shape.

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

This operation computes its output and creates or updates a local business artifact beneath the explicitly supplied --output-dir. Effect: `local_knowledge_index_update`.

Report the actual command output and, when present, its effect receipt. A nonzero exit
means the operation failed. This package executes only its declared operation.

The implementation is scripts/operation.py, input/output validation is
scripts/validation.py, and role configuration is scripts/config.json. All Python
dependencies are from the standard library. Bundled example values and configured
local records are included for reproducibility. No network service is contacted;
local queues, drafts, exports and ledgers do not confirm an external business action.
