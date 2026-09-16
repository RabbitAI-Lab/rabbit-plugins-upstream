## Description:

Helps agents operate Softr through OOMOL's oo CLI for reading, creating, updating, and deleting Softr data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Softr databases, tables, fields, views, and records, and to create, update, or delete records through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer one-liners for the OOMOL CLI.

Mitigation: Prefer verified installation instructions and avoid automatic execution of remote installer commands.

Risk: The connector can create, update, and delete Softr records.

Mitigation: Require explicit user confirmation for exact payloads and targets before any write or destructive action.

Risk: Use depends on trusting OOMOL's CLI distribution and account connection.

Mitigation: Install only in environments where that CLI and connected Softr access are approved.

## Reference(s):

- [Softr homepage](https://www.softr.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-softr)
- [Skill icon](https://static.oomol.com/logo/third-party/softr.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before connector calls; write and destructive operations require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
