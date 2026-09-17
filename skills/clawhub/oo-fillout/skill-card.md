## Description:

Fillout (fillout.com). Use this skill for ANY Fillout request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Fillout forms and submissions through an OOMOL-connected account. It supports listing forms, reading form metadata and submissions, creating submissions, and deleting submissions after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer scripts executed directly in a shell.

Mitigation: Use the official oo CLI documentation to download and verify the installer before running it.

Risk: The skill can create and delete Fillout submissions in the connected account.

Mitigation: Confirm the exact payload for create actions and the exact target submission for delete actions before execution.

Risk: Connector access depends on the Fillout account permissions connected through OOMOL.

Mitigation: Install and use the skill only when the OOMOL connection is trusted and scoped appropriately for the intended Fillout account.

## Reference(s):

- [Fillout homepage](https://www.fillout.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fillout)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Fillout connector actions through the oo CLI and return connector JSON responses.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
