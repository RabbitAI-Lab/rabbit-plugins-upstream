## Description:

Records a timezone-aware service capacity window and reports available slots and scheduling overlaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service planners and operations teams use this skill to record a requested capacity window and check available slots and overlaps against bundled local records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates or updates a local SQLite capacity ledger in the chosen output directory.

Mitigation: Choose a dedicated writable output directory and review the resulting ledger entry.

Risk: Local capacity records do not confirm an external reservation or other business action.

Mitigation: Check capacity and scheduling decisions against the authoritative service before acting on them.

## Reference(s):

- [Capacity Ledger Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/service-capacity-window-workbench)
- [Package usage and local output](artifact/README.md)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON capacity ledger entry and local SQLite ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes available and reserved slots, capacity and overlap statuses, and a receipt for the local ledger artifact.]

## Skill Version(s):

1.1.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
