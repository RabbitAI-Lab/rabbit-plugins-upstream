## Description:

Records a capacity-window entry and reports available slots and scheduling overlaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service planners and operations staff use this skill to record a timezone-aware capacity window and review available slots, reservations, and scheduling overlaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive capacity records and local artifact paths automatically.

Mitigation: Review delivery settings before installation; use only a trusted, intended endpoint, or leave delivery environment variables unset for local-only operation.

Risk: The operation writes local capacity records.

Mitigation: Choose a dedicated, writable output directory for the ledger.

## Reference(s):

- [Capacity Ledger Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/service-capacity-window-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON capacity ledger entry and receipts; local ledger file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes capacity and overlap status; delivery receipt indicates whether remote submission was configured.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
