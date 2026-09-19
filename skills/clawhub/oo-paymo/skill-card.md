## Description:

Paymo (paymoapp.com). Use this skill for Paymo requests such as reading, creating, updating, and deleting clients, projects, and tasks through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Paymo through the oo CLI, including listing, retrieving, creating, updating, and deleting Paymo clients, projects, and tasks after confirming state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path uses remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI from a verified package or documented release when possible, and validate checksums or signatures before running installer scripts.

Risk: Paymo write and destructive actions can create, modify, or delete client, project, and task data.

Mitigation: Confirm the exact payload, target record, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-paymo)
- [Paymo homepage](https://www.paymoapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector schema and run commands; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
