## Description:

Mendeley lets an agent read, create, update, search, and delete documents in an authorized Mendeley library through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Mendeley library records and look up public Mendeley catalog metadata after the user has connected the account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or permanently delete records in a connected Mendeley library.

Mitigation: Require explicit user confirmation for the exact payload and target before write or destructive actions.

Risk: First-time setup may install the oo CLI if it is missing.

Mitigation: Use the installer only when the CLI is not already present and the user accepts that setup step.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mendeley)
- [Mendeley Homepage](https://www.mendeley.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution; read actions are safe by default while write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
