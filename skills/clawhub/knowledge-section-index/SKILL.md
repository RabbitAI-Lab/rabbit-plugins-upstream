---
name: knowledge-section-index
description: Combines segment a knowledge note for indexing with update a section and backlink index.
version: 1.0.7
metadata:
  openclaw:
    skillKey: knowledge-section-index
---

# Knowledge Note Segmenter and Knowledge Index Curator

Use this skill for routine knowledge operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Knowledge Note Segmenter

Tool: `segment_knowledge_note`

Reads knowledge notes and prepares referenced sections, tags, and links for indexing.

Input field: `knowledge_note`. Knowledge note with a reference, headings, tags, and related links.

Output field: `segmented_note`.

## Operation 2: Knowledge Index Curator

Tool: `update_knowledge_index`

Updates a local knowledge index with section digests and backlink relationships.

Input field: `segmented_note`. Referenced note sections prepared for the shared knowledge index.

Output field: `index_update`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
