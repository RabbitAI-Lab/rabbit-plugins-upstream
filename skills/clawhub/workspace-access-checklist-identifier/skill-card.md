## Description:

Compares current and approved workspace access lists to identify membership and role differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and collaborators use this skill to compare current membership with an approved list, identifying added or removed members, role changes, and external entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace membership lists may contain sensitive access information.

Mitigation: Only provide membership lists you are authorized to share with the local comparator.

## Reference(s):

- [Workspace Access Comparator on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-access-checklist-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The access_delta contains workspace_id, added, removed, role_changed, and external_entries.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
