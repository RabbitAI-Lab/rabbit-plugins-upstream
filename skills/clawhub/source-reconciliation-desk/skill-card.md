## Description:

Sets source-agreement guidance and resolves imported field values using that guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams reconciling imported business fields use this skill to set agreement rules and resolve conflicting source values. The downstream operation can save a local resolution record for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream operation creates local CSV artifacts.

Mitigation: Use a dedicated output directory and review the generated source resolution and effect receipt.

Risk: Incorrect source guidance or resolution could affect business decisions.

Mitigation: Review the guidance and selected values against the underlying sources before relying on them.

## Reference(s):

- [Source Reconciliation Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/source-reconciliation-desk)

## Skill Output:

**Output Type(s):** [Guidance, JSON, CSV files]

**Output Format:** [Text guidance or JSON resolution with optional local CSV artifact and effect receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation writes a CSV under a user-chosen output directory; the upstream operation does not persist an artifact.]

## Skill Version(s):

3.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
