## Description:

This skill lets an agent handle Softr requests, including reading, creating, updating, and deleting Softr data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Softr schemas and perform database, table, view, and record operations through an OOMOL-connected Softr account. It supports read workflows as well as confirmed record creation, update, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that execute downloaded shell or PowerShell code.

Mitigation: Review the installer source and trust boundary before running it; prefer a verified, versioned installer or official package-manager flow when available.

Risk: The skill can create, update, and delete Softr records through the connected account.

Mitigation: Confirm the exact action, target record or table, and payload with the user before any write or destructive operation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-softr)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Softr Homepage](https://www.softr.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Softr connector actions through the oo CLI; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
