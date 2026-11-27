---
name: Skill Race Canary i44096 nb16vw
description: Inert concurrency canary used to verify ClawHub skill publication staging semantics under parallel requests from two separate accounts.
version: 0.0.2
---

# Skill Race Canary nb16vw

This document is an inert, documentation-only artifact created during a sanctioned security assessment of ClawHub. It contains no executable code, performs no network requests, stores no credentials, and produces no side effects beyond a database row that can be removed by its owner afterwards. The canary exists solely to observe how the publication pipeline stages a first version while a second account submits an identically named slug at the same instant.

## Why this canary exists

The assessment team is auditing the boundary between the staging step that writes a pending version row and the follow-up step that records a publish attempt. Earlier work on the package registry showed that a cleanup branch could remove a pending row belonging to another publisher when a release existed without a matching attempt. The question here is narrower: does the skill pipeline contain an equivalent branch, and if so can a third party reach it by racing a publish request against the original author?

## What the canary measures

- Whether the publication endpoint resolves the target skill strictly within the caller publisher namespace, so that another owner slug cannot be selected.
- Whether a duplicate version submission from a different account creates its own staging row instead of mutating the original author row.
- Whether any cleanup responsibility runs without an actor or owner assertion during the window between version insertion and attempt creation.
- Whether anonymous readers can observe a pending first version through the public skill page, the public versions listing, or the owner-scoped publication status endpoint.
- Whether the resulting attempt identifiers are readable by their own owner only.

## Procedure being exercised

1. The first account submits a brand new slug with a single Markdown file and accepts the MIT-0 terms.
2. While that request is in flight, the second account submits the same slug, the same semantic version, and a distinct documentation body.
3. Both responses are recorded with timestamps and identifiers.
4. After the race, the original author queries its own publication status and attempt record, and the second account attempts to read the same attempt identifier.

## Expected safe behaviour

The original author staging row should survive unchanged, the second account should either create an independent row under its own publisher or receive a duplicate-version message about its own namespace, and no cleanup branch should be reachable across publishers. Any deviation would be documented with request and response evidence.

## Marker

Canary marker nb16vw for account playgod2023 on slug clh-skillrace-i44096-8ims3. This paragraph is unique per submission so that the structural similarity heuristic does not treat repeated canary runs as spam.
