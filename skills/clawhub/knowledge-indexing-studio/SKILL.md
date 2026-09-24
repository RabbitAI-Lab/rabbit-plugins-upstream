---
name: knowledge-indexing-studio
description: Segment knowledge notes and update the knowledge-base index.
version: 1.0.0
metadata:
  openclaw:
    skillKey: knowledge-indexing-studio
---

# Knowledge Indexing Studio

Use this skill for routine knowledge operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for knowledge operations work:

1. **Segment a knowledge note for indexing** with the `segment_knowledge_note` tool, producing `segmented_note`.
2. **Update a section and backlink index** with the `update_knowledge_index` tool, using the prepared `segmented_note` and producing `index_update`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Segment a knowledge note for indexing

Purpose: Segment a knowledge note for indexing.

Tool: `segment_knowledge_note`

Interface fields: input `knowledge_note`; output `segmented_note`.

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

## 2. Update a section and backlink index

Purpose: Update a section and backlink index.

Tool: `update_knowledge_index`

Interface fields: input `segmented_note`; output `index_update`.

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
