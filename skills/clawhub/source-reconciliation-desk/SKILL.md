---
name: source-reconciliation-desk
description: Derive source agreement rules and resolve conflicting source values.
version: 1.0.0
metadata:
  openclaw:
    skillKey: source-reconciliation-desk
---

# Source Reconciliation Desk

Use this skill for routine source reconciliation work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for source reconciliation work:

1. **Set source-agreement guidance** with the `derive_source_agreement_rule` tool, producing `source_guidance`.
2. **Resolve imported field values** with the `resolve_source_values` tool, using the prepared `source_guidance` and producing `source_resolution`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Set source-agreement guidance

Purpose: Set source-agreement guidance.

Tool: `derive_source_agreement_rule`

Interface fields: input `source_profile`; output `source_guidance`.

Use this skill for routine source reconciliation work when the user
asks to set source-agreement guidance.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `source_profile`

Source count, field importance, and disagreement preference.

Accepted value: object.

### Output

Field: `source_guidance`

Return a concise source guidance for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied source_profile to set source-agreement guidance.
Return the result in source_guidance.
```

## 2. Resolve imported field values

Purpose: Resolve imported field values.

Tool: `resolve_source_values`

Interface fields: input `source_guidance`; output `source_resolution`.

Use this skill for routine source reconciliation work when the user
asks to resolve imported field values.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `source_guidance`

Source-agreement guidance available from the active intake session.

Accepted value: string or object with `required_agreement`, `conflict_action` or object with `cue`.

### Output

Field: `source_resolution`

Return a concise source resolution for the user's current request in the requested
output field. The returned value is a object with `field`, `disposition`, `selected_value`, `agreement_count`.

### Example Request

```text
Use the supplied source_guidance to resolve imported field values.
Return the result in source_resolution.
```
