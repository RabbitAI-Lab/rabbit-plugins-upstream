## Description:

Merges an account revision using supplied field guidance and records the result locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People maintaining account records use this skill to merge incoming revisions while preserving fields according to supplied guidance and recording the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merged account records can be sent to an external service when a delivery endpoint is configured.

Mitigation: Run without delivery endpoint or related credential variables unless external transmission is explicitly approved; review the destination and merged record before enabling delivery.

Risk: Applying field guidance can change account values and create local merge artifacts.

Mitigation: Review the proposed changes and use a dedicated writable output directory before running the merge.

## Reference(s):

- [Account Merge Workbench on ClawHub](https://clawhub.ai/wxt-ai/skills/revision-handling-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON merge result and local account record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports changed and preserved fields, a local artifact receipt, and delivery status when applicable.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
