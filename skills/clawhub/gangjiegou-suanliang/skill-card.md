## Description:

Turns steel geometry contract JSON into reviewable steel tonnage estimates; it does not read drawings or replace final quantity settlement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Structural estimators and engineers use this skill to calculate reviewable steel tonnage bands from existing steel geometry contract JSON and inspect section, member, connection, and finish summaries. Its estimates support review and do not replace final quantity settlement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a partial scan, so the scan evidence is incomplete.

Mitigation: Review the complete release bundle before installing or running the skill.

Risk: The security review flags a mismatch between the stated no-drawing-recognition boundary and a workflow that includes drawing recognition.

Mitigation: Review the CAD reader dependency and confirm the workflow keeps drawing recognition in that dependency and passes this skill only steel geometry contract JSON.

Risk: evidence.json reports MIT-0, while the release manifest and LICENSE.md name CC-BY-NC-SA-4.0.

Mitigation: Confirm the authoritative license before redistribution or commercial use.

## Reference(s):

- [lis-skill-bus contract reference](references/bus-contract.md)

## Skill Output:

**Output Type(s):** [Analysis, Files]

**Output Format:** [JSON, Markdown, and CSV report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [±15% estimate bands; final_quantity=false; results require review and do not replace design, quantity settlement, or pricing.]

## Skill Version(s):

0.3.8 (source: frontmatter, changelog, released 2026-11-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
