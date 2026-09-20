## Description:

Enables an agent to read, create, update, and delete MaintainX data through the OOMOL oo CLI instead of calling the MaintainX API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operations teams, and developers use this skill to manage MaintainX locations, users, work orders, statuses, and comments from an agent session. It supports read workflows as well as confirmed write and destructive workflows against business-maintenance data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run an unverified remote installer if the oo CLI is missing.

Mitigation: Review and install the oo CLI from a trusted, versioned source before agent use, then restrict the agent to scoped oo connector commands.

Risk: MaintainX write and delete actions can change or remove business-maintenance records.

Mitigation: Require explicit user confirmation of the target record, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-maintainx)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [MaintainX homepage](https://www.getmaintainx.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce scoped oo connector commands and request user confirmation for write or destructive MaintainX actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
