## Description:

Softr helps an agent read, create, update, and delete Softr data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they need an agent to work with Softr databases, tables, fields, views, and records. It supports read workflows and state-changing record creation, update, and deletion through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing Softr actions can create or modify records.

Mitigation: Review the exact payload and expected effect with the user before running create or update actions.

Risk: The delete action can permanently remove a Softr record.

Mitigation: Confirm the specific target record and get explicit approval before running destructive actions.

Risk: The connected Softr credential may expose more data than the task requires.

Mitigation: Use a Softr token scoped no broader than needed for the intended databases and tables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-softr)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Softr homepage](https://www.softr.io/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent should inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
