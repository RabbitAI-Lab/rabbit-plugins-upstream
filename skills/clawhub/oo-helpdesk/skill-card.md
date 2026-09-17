## Description:

HelpDesk (helpdesk.com). Use this skill for ANY HelpDesk request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and operations users can use this skill to manage HelpDesk tickets through an OOMOL-connected account. It supports reading and searching tickets, listing agents and teams, and running confirmed write or destructive ticket actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer pipelines that can execute arbitrary code if the installer source is not trusted.

Mitigation: Review before installing and verify the oo CLI installer through a safer trusted channel before running remote install commands.

Risk: The skill can create, update, move, or delete HelpDesk tickets.

Mitigation: Use a least-privileged HelpDesk connection and confirm the exact payload and effect before every write or destructive action.

## Reference(s):

- [ClawHub HelpDesk Skill](https://clawhub.ai/oomol/skills/oo-helpdesk)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [HelpDesk Homepage](https://www.helpdesk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [HelpDesk Skill Icon](https://static.oomol.com/logo/third-party/helpdesk.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use live connector schemas and return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
