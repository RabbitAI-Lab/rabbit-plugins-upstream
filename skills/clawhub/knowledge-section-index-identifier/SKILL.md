---
name: knowledge-section-index-identifier
description: Segment a knowledge note for indexing.
version: 1.0.7
metadata:
  openclaw:
    skillKey: knowledge-section-index-identifier
---

# Knowledge Note Segmenter

Use this skill for routine knowledge operations work when the user
asks to segment a knowledge note for indexing.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `knowledge_note`

Knowledge note with a reference, headings, tags, and related links.

Accepted value: string.

## Output

Field: `segmented_note`

Return a concise segmented note for the user's current request in the requested
output field. The returned value is a object with `reference`, `heading`, `tags`, `links`, `content_digest`, `sections`.

## Example Request

```text
Use the supplied knowledge_note to segment a knowledge note for indexing.
Return the result in segmented_note.
```
