## Description:

Analyzes DWG/DXF structural drawings to estimate concrete quantities and rebar planning ranges by floor and pour zone, with quantity checks and planning-only limitations.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Construction engineers and estimators use the skill to turn structural drawings into preliminary concrete and rebar material plans organized by floor and pour zone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The offline setting may still allow dependency setup to run.

Mitigation: Review the CAD dependency and setup behavior before running, and do not rely on SKILL_NO_BASE=1 alone for offline operation.

Risk: Reports may present unverified assumptions as confirmed results.

Mitigation: Use results only as preliminary estimates; have an experienced reviewer independently verify beam coverage, concrete grades, slab thickness, and column geometry before ordering materials.

Risk: Retained drawing caches and optional shared project state may contain sensitive project information.

Mitigation: Protect retained caches and limit access to shared project state.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, CSV, JSON, Files]

**Output Format:** [Quantity summaries and review notes in Markdown, CSV, and JSON, with optional Excel reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning estimates only; the artifact describes typical quantity ranges of about ±5–10% and excludes bar detailing, cutting, reconciliation, settlement, and final measurement.]

## Skill Version(s):

0.9.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
