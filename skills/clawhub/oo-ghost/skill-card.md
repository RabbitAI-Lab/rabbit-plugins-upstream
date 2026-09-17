## Description:

Ghost (ghost.org). Use this skill for Ghost requests that read, create, or update data through the OOMOL-connected oo CLI instead of calling the Ghost API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Ghost site through OOMOL, including reading published posts, pages, authors, tags, and settings and preparing confirmed state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup asks users to execute a remote installer script for the oo CLI.

Mitigation: Review the OOMOL CLI installation path first and prefer a signed or checksum-verified installer when available.

Risk: Connecting Ghost through OOMOL lets the connector act on the connected site according to granted scopes.

Mitigation: Grant only the scopes needed for the intended tasks and confirm payloads before running write or destructive actions.

Risk: Live connector actions can change Ghost site state when an action is tagged write or destructive.

Mitigation: Inspect the live action schema and obtain explicit user confirmation for the exact payload and effect before state-changing actions.

## Reference(s):

- [ClawHub Ghost Skill](https://clawhub.ai/oomol/skills/oo-ghost)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Ghost Homepage](https://ghost.org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
