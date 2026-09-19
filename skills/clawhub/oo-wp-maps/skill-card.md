## Description:

Operates WP Maps through OOMOL's wp_maps connector so agents can read, create, update, and delete stores and products after inspecting the live action schema.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage WP Maps stores and products from an agent through the OOMOL CLI. It is suited for read workflows and for confirmed write or delete workflows against a connected WP Maps account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete WP Maps data through the connected OOMOL account.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit approval for destructive actions.

Risk: The security review flags remote installer commands and broad OOMOL CLI command access.

Mitigation: Install the oo CLI only from a trusted, verified source, prefer pinned or inspected installers, and restrict execution to documented wp_maps connector commands.

## Reference(s):

- [ClawHub WP Maps skill page](https://clawhub.ai/oomol/skills/oo-wp-maps)
- [WP Maps homepage](https://wpmaps.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before executing actions; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
