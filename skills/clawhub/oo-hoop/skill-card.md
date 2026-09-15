## Description:

Hoop (hoop.dev). Use this skill for ANY Hoop request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Hoop action schemas and run read-oriented Hoop connector actions through an OOMOL-connected oo CLI session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running an internet installer for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, reviewable path, verify integrity if available, and personally approve installer execution.

Risk: Hoop queries are routed through an OOMOL-connected CLI session.

Mitigation: Use the skill only when comfortable routing Hoop queries through OOMOL, and personally approve sign-in, Hoop connection, and billing-related steps.

## Reference(s):

- [ClawHub Hoop skill page](https://clawhub.ai/oomol/skills/oo-hoop)
- [Hoop homepage](https://hoop.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hoop connector responses are returned as JSON when the documented oo CLI command is run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
