## Description:

Botpress (botpress.com). Use this skill for ANY Botpress request - searching and reading data. Whenever a task involves Botpress, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Botpress workspaces and bots through an OOMOL-connected Botpress account. It supports read-oriented Botpress discovery workflows, including listing accessible workspaces, listing bots, and retrieving details for an individual bot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands for the OOMOL oo CLI.

Mitigation: Inspect installer scripts first or use a verified, versioned installer, and avoid elevated privileges during setup.

Risk: The skill depends on a connected OOMOL account and Botpress credentials managed outside the skill.

Mitigation: Install only when the publisher and account connection are trusted, and retry setup steps only after authentication or connection failures.

## Reference(s):

- [ClawHub Botpress skill release](https://clawhub.ai/oomol/skills/oo-botpress)
- [Botpress homepage](https://botpress.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the OOMOL oo CLI to fetch Botpress connector schemas and run read actions; command responses are JSON when --json is used.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
