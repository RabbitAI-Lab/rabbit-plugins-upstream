---
name: stakeholder-briefing-studio
description: Advise audience readiness and compose circulation-ready briefs.
version: 1.0.0
metadata:
  openclaw:
    skillKey: stakeholder-briefing-studio
---

# Stakeholder Briefing Studio

Use this skill for routine stakeholder communications work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for stakeholder communications work:

1. **Set the intended audience for a briefing** with the `advise_audience_readiness` tool, producing `audience_mode`.
2. **Compose audience-ready briefing sections** with the `compose_client_brief` tool, using the prepared `audience_guidance` and producing `briefing_preview`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set the intended audience for a briefing

Purpose: Classify a stakeholder brief by audience and define which sections are ready for client circulation.

Tool: `advise_audience_readiness`

Interface fields: input `audience_request`; output `audience_mode`.

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

## 2. Compose audience-ready briefing sections

Purpose: Build a client-facing brief from approved sections while recording omissions for internal follow-up.

Tool: `compose_client_brief`

Interface fields: input `audience_guidance`; output `briefing_preview`.

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
