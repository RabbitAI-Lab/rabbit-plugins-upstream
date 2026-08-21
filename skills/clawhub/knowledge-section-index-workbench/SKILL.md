---
name: knowledge-section-index-workbench
description: Update a section and backlink index.
version: 1.0.7
metadata:
  openclaw:
    skillKey: knowledge-section-index-workbench
---

# Knowledge Index Curator

Use this skill for routine knowledge operations work when the user
asks to update a section and backlink index.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `segmented_note`

Referenced note sections prepared for the shared knowledge index.

Accepted value: object with `reference`, `heading`, `tags`, `links`, `content_digest`, `sections`.

## Output

Field: `index_update`

Return a concise index update for the user's current request in the requested
output field. The returned value is a object with `index_id`, `reference`, `heading`, `content_digest`, `indexed_sections`, `backlinks`, `dedup_status`, `duplicates_removed`.

## Example Request

```text
Use the supplied segmented_note to update a section and backlink index.
Return the result in index_update.
```
