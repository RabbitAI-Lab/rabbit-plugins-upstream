---
name: audience-readiness-guidance-workbench
description: Build a client-facing brief from approved sections while recording omissions for internal follow-up.
version: 1.0.7
metadata:
  openclaw:
    skillKey: audience-readiness-guidance-workbench
---

# Client Brief Composer

Prepare a circulation-ready brief from `audience_guidance` and the sections
available in the current communications request.

## Assembly sequence

First resolve the audience named by the guidance. Then classify each candidate
section by its declared tag or purpose. Include only sections permitted for that
audience, keep their source order unless the request specifies another order,
and remove drafting annotations from the rendered preview. Do not invent facts
to fill a missing section.

## Briefing preview contract

Return `briefing_preview` with:

- `audience`: the audience actually used;
- `included_sections`: the section identifiers placed in the brief;
- `excluded_sections`: omitted identifiers together with a short reason.

The exclusion list is an operational handoff, not client-facing prose. It lets
the communications owner see why a section was left out and decide whether to
approve or revise it later.

## Practical example

Given a client-ready rule and sections tagged `approved-progress`,
`internal-estimate`, and `agreed-next-step`, compose the preview from the first
and third sections. Record the estimate in `excluded_sections` as internal
working material.

## Completion check

Before returning the object, confirm that every supplied section appears in
exactly one of the included or excluded lists and that the selected audience
matches the guidance.

## Interface reference

Input field: `audience_guidance`. Audience guidance available from the active communications session.

Accepted value: string or object with `audience`, `allowed_section_tags` or object with `cue`.

Output field: `briefing_preview`; the returned value is a
object with `audience`, `included_sections`, `excluded_sections`.

This standalone documentation does not require credentials or access to private files.
