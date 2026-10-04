## Description:

Compare supplied current and approved workspace access lists to identify membership and role differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and collaboration teams use this skill to compare supplied current and approved member lists, highlighting added or removed members, changed roles, and external entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace membership lists may contain sensitive access information, and results reflect only the lists supplied.

Mitigation: Review the input before running the local comparison, restrict who can see the lists and resulting delta, and confirm reported differences against authoritative access records before acting.

## Reference(s):

- [Workspace Access Comparator on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-access-checklist-identifier)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON object in the access_delta field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes workspace_id, added, removed, role_changed, and external_entries; no access changes are made.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
