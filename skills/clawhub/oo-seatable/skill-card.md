## Description:

SeaTable (seatable.com). Use this skill for ANY SeaTable request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected SeaTable base through OOMOL, including listing rows, retrieving metadata, appending rows, updating rows, and deleting rows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete rows in the connected SeaTable base.

Mitigation: Confirm the exact target rows, payload, and expected effect before approving write or destructive actions.

Risk: The skill depends on the oo CLI and an OOMOL-connected SeaTable account.

Mitigation: Install and authenticate the CLI only when needed, and verify the install command before running it.

## Reference(s):

- [SeaTable homepage](https://seatable.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-seatable)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce SeaTable connector calls and JSON responses through the oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
