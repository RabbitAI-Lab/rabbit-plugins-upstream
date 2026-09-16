## Description:

Typebot (typebot.com). Use this skill for ANY Typebot request - searching and reading data. Whenever a task involves Typebot, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to discover and read Typebot workspaces, bots, bot definitions, and collected results through an OOMOL-connected Typebot account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes one-line remote installer commands that pipe scripts directly into a shell.

Mitigation: Prefer installing the oo CLI from a trusted, verifiable release path and avoid piping remote scripts directly into a shell.

Risk: The listed Typebot actions are read-oriented, but future or schema-discovered actions may change Typebot state.

Mitigation: Require explicit confirmation before running any action that writes, overwrites, or deletes Typebot data.

## Reference(s):

- [ClawHub Typebot Skill](https://clawhub.ai/oomol/skills/oo-typebot)
- [Typebot Homepage](https://typebot.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; read actions return JSON data from Typebot through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
