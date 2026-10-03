## Description:

Create an access review checklist from supplied workspace membership changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Collaboration operations teams use supplied workspace membership changes to prepare a local access-review checklist for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace membership differences may contain sensitive access information.

Mitigation: Provide only the necessary membership data and review the checklist before sharing it.

Risk: Running the skill creates or updates local YAML checklist files.

Mitigation: Choose a dedicated, writable output directory and review existing files before running it.

## Reference(s):

- [Access Review Checklist on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-access-checklist-workbench)

## Skill Output:

**Output Type(s):** [JSON, YAML checklist]

**Output Format:** [JSON checklist result and local YAML checklist file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a checklist identifier, workspace identifier, items, and a local file receipt.]

## Skill Version(s):

1.1.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
