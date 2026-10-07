## Description:

Creates an access review checklist from workspace membership changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and collaboration teams use this skill to turn membership additions, removals, role changes, and external entries into an access review checklist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive access-review details may be sent to an external service when delivery settings are present, including generic environment variables not clearly disclosed in the skill instructions.

Mitigation: Review delivery environment variables before installation, restrict outbound network access, and require approval of any configured delivery endpoint.

## Reference(s):

- [Access Review Checklist on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-access-checklist-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON checklist response and local YAML artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes checklist ID, workspace ID, review items, and an optional delivery receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
