## Description:

Landbot lets agents read Landbot workspace data and send or update customer messages through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Landbot customer messaging workflows through OOMOL, including listing channels and customers, fetching customer messages, sending text messages, and setting customer fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts directly in a shell.

Mitigation: Install only from a trusted OOMOL CLI distribution path, prefer a verified package or installation guide, and inspect installer scripts before running them.

Risk: Write actions can send text messages or update typed custom fields in Landbot.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Landbot skill page](https://clawhub.ai/oomol/skills/oo-landbot)
- [Landbot homepage](https://landbot.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
