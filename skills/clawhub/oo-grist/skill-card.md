## Description:

Grist (getgrist.com). Use this skill for Grist requests, including reading, creating, updating, and deleting data through the OOMOL Grist connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Grist through an OOMOL-connected account, including listing workspaces, documents, tables, columns, and records. The skill also supports adding, updating, and deleting Grist records with user confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer one-liners can execute unverified code during setup.

Mitigation: Install the OOMOL CLI only through a trusted, verified method and do not let an agent run remote installer commands automatically.

Risk: Write and destructive Grist actions can change or delete user data.

Mitigation: Confirm the exact payload, target document or table, and expected effect before writes; require explicit approval before delete operations.

## Reference(s):

- [ClawHub Grist Skill](https://clawhub.ai/oomol/skills/oo-grist)
- [Grist Homepage](https://www.getgrist.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
