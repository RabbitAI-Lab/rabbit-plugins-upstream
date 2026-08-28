## Description:

dig refines an active research session by drilling deeper into a subtopic and narrowing results to a specific channel or angle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill after an initial tome research session to drill into a narrower subtopic, optionally filtering by a channel such as papers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects an existing tome research session and may fail or produce irrelevant refinement without one.

Mitigation: Start with tome:research and verify the active session before using dig.

Risk: The skill may update the saved report for the active session as part of normal refinement.

Mitigation: Review new findings before relying on or sharing the updated report.

## Reference(s):

- [Tome plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/tome)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown research findings and session-update guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update the active session's saved report as part of normal use.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
