## Description:

WP Maps (wpmaps.com) lets an agent read, create, update, and delete WP Maps stores and products through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage WP Maps account data, including stores and products, while confirming write and destructive changes before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and delete actions can change or remove WP Maps account data.

Mitigation: Confirm the exact payload, target records, and expected effect with the user before running write or destructive actions.

Risk: First-time setup includes remote shell installer commands.

Mitigation: Use an official package or downloaded installer with checksum or signature verification, and review installer behavior before executing it.

Risk: Connector payload fields may differ from static examples.

Mitigation: Inspect the live connector schema before constructing action payloads.

## Reference(s):

- [WP Maps homepage](https://wpmaps.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wp-maps)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
