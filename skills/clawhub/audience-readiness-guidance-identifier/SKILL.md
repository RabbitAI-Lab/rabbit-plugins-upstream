---
name: audience-readiness-guidance-identifier
description: Classify a stakeholder brief by audience and define which sections are ready for client circulation.
version: 1.0.7
metadata:
  openclaw:
    skillKey: audience-readiness-guidance-identifier
---

# Audience Readiness Guide

This skill turns an `audience_request` into an explicit audience rule for a
stakeholder briefing. Use it before a composer selects material for circulation.

## Audience choices

- **Client-ready**: approved outcomes, agreed dates, and externally supported
  explanations.
- **Executive**: decisions, material risks, owners, and concise next steps.
- **Internal working**: unresolved questions, drafting notes, dependencies, and
  operational detail.

## How to classify a request

Identify the named recipients and the purpose of the briefing. If the request
does not name an audience, use the surrounding delivery context rather than
assuming that draft material is ready for external circulation. Record which
section tags belong in the selected view and which tags must remain outside it.

## Output rule

Return `audience_mode` as a short policy string. It should name the chosen
audience, list the section classes that may be included, and state how to handle
unapproved or ambiguous material. Keep the rule usable by a later briefing
composer without rewriting the source brief.

## Sample decision

An account update requested for a customer meeting can yield a client-ready
mode that includes approved progress, confirmed dates, and agreed actions while
holding internal estimates and unresolved ownership notes for follow-up.

## Interface reference

Input field: `audience_request`. Stakeholder brief, account update, or communications handoff.

Accepted value: object.

Output field: `audience_mode`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.
