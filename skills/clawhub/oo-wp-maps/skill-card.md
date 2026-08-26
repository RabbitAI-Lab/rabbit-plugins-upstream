## Description:

WP Maps (wpmaps.com). Use this skill for ANY WP Maps request - reading, creating, updating, and deleting data. Whenever a task involves WP Maps, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read and manage WP Maps stores and products through an OOMOL-connected account, with schema inspection before action execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete WP Maps products and stores through the connected account.

Mitigation: Review write and delete payloads with the user and obtain explicit approval before running state-changing or destructive actions.

Risk: Setup commands and account connection steps affect the user's OOMOL environment and billing readiness.

Mitigation: Run install, login, connection, or billing recovery steps only after a relevant command failure and only when the user intends to use the connector.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wp-maps)
- [WP Maps homepage](https://wpmaps.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
