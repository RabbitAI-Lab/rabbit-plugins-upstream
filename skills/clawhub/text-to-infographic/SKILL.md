---
name: text-to-infographic
version: 1.1.2
description: Organizes user-provided content into a structured single-page infographic specification and copyable standalone HTML source. Invoke when the user explicitly requests either deliverable.
---

# Text to Infographic

## Scope

This skill produces either or both of:

1. Organize content already provided by the user into a structured specification for a single-page infographic.
2. Represent that specification as copyable, standalone HTML source.

Boundary: **current conversation content only / no side effects**. Use supplied facts and constraints without external enrichment or state changes.

## Activation examples

Invoke for requests such as:

- "Turn these notes into a one-page infographic specification."
- "Create standalone HTML for this infographic."
- "Organize this supplied comparison into an infographic layout."

Do not invoke for ordinary summaries, slide decks, multi-page reports, image editing, data collection, or requests that do not explicitly ask for an infographic specification or standalone infographic HTML.

## Input

- Source content to organize.
- An optional title or intended reading context.
- Optional visual constraints such as dimensions, orientation, density, palette, typography, hierarchy, or accessibility requirements.
- Optional factual labels, source notes, or attribution text already present in the supplied content.

Keep missing facts, values, citations, assets, and preferences unspecified.

## Output contract

### 1. Single-Page Infographic Specification

- Title and optional subtitle.
- Communication objective.
- Intended reading order.
- Section hierarchy.
- Content blocks mapped only from supplied material.
- Recommended visual form for each block, such as text, metric, comparison, sequence, timeline, matrix, or diagram.
- Layout, spacing, color, typography, and accessibility notes.
- Source-note and attribution placement when such text is supplied.
- A concise inventory linking every displayed claim to the supplied content.

### 2. Standalone HTML Source

- A complete document beginning with `<!doctype html>`.
- Copyable as one uninterrupted source block.
- Limited to HTML and inline CSS.
- Self-contained and static.
- Suitable for static display as one page.
- Semantically structured and readable without visual styling.
- Inclusive of print-safe styling when print presentation is requested in the supplied constraints.

## Validation Checklist

- The frontmatter name is `text-to-infographic`.
- The frontmatter version is `1.1.2`.
- Every factual statement in the output is traceable to user-provided content.
- The result describes exactly one page.
- The specification includes objective, hierarchy, reading order, content mapping, and visual guidance.
- The HTML is a complete document and is presented as copyable source.
- All CSS is inline within the HTML document.
- The HTML has no active behavior or external dependency.
- Claims, citations, and metrics remain grounded in supplied content.
- Text remains available in semantic HTML rather than only as decorative graphics.
- Color is not the sole carrier of meaning.
- Heading order and reading order are coherent.
