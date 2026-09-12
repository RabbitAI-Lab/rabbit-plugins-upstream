## Description:

HaiGuanJia helps agents operate HaiGuanJia through OOMOL's oo CLI connector for customs, manifest, schedule, container, recognition, and tracking workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route HaiGuanJia requests through an OOMOL-connected account for reading, creating, updating, deleting, and resubmitting logistics and customs data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may involve direct remote installer execution.

Mitigation: Install only after trusting OOMOL and the workflow; prefer a verified package or reviewed installer and avoid elevated shells.

Risk: Write, delete, subscription, and chargeable actions can change HaiGuanJia data or incur business charges.

Mitigation: Confirm the exact action, target, payload, and cost implications with the user before execution.

Risk: The skill operates through connected OOMOL and HaiGuanJia account access.

Mitigation: Use only authorized account data, do not request raw tokens, and rely on the connector-managed credential flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hgj)
- [HaiGuanJia OpenAPI](https://openapi.hgj.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId; write, destructive, subscription, and chargeable actions require confirmation before execution.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
