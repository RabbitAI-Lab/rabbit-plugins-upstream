---
name: draft-precedence-guidance-identifier
description: Select the highest approved document version within the requested major release line.
version: 1.0.7
metadata:
  openclaw:
    skillKey: draft-precedence-guidance-identifier
---

# Document Release Guide

Derive a release-selection rule from `release_profile`. This is useful when a
document repository contains drafts, approved revisions, and versions from
several major release lines.

## Eligibility gate

A candidate is eligible only when its approval state satisfies the profile and
its major version matches the requested release line. Exclude withdrawn,
superseded, or draft-only candidates unless the request explicitly permits
them. A newer timestamp does not override an ineligible approval state.

## Precedence within the line

Compare semantic versions numerically. Select the greatest approved version in
the requested major line, using approval time only to resolve duplicate records
for the same version. If no candidate is eligible, return a no-selection rule
with the missing requirement.

## Output

Return `selection_guidance` as a concise string describing the eligibility
gate, the version ordering, the duplicate tie-breaker, and the no-selection
condition. The guide chooses a rule; it does not publish or overwrite a
document.

## Worked case

For requested major version 3, approved `3.4.1` outranks approved `3.3.9`.
Draft `3.5.0` remains ineligible, and approved `4.0.0` belongs to a different
release line.

## Interface reference

Input field: `release_profile`. Current release line and candidate eligibility preference.

Accepted value: object.

Output field: `selection_guidance`; the returned value is a
string.

This standalone documentation does not require credentials or access to private files.
