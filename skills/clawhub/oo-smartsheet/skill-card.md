## Description:

Use this skill for Smartsheet requests to read, create, update, and delete data through an OOMOL-connected Smartsheet account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to let an agent operate Smartsheet sheets through an OOMOL-connected account, including listing sheets, reading sheet data, and adding, updating, or deleting rows with confirmation safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI through a verified, pinned, or otherwise trusted method.

Risk: The skill can add, update, and delete Smartsheet rows through an authenticated account.

Mitigation: Confirm every write or delete operation against the exact sheet, row target, and JSON payload before execution.

## Reference(s):

- [ClawHub Smartsheet skill page](https://clawhub.ai/oomol/skills/oo-smartsheet)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Smartsheet homepage](https://www.smartsheet.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and JSON action payloads; state-changing Smartsheet actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
