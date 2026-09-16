## Description:

Xweather (xweather.com). Use this skill for ANY Xweather request -- searching and reading data. Whenever a task involves Xweather, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Xweather forecasts, current observations, and place-resolution data through an OOMOL-connected account without directly handling raw Xweather API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified internet installer scripts for the OOMOL CLI.

Mitigation: Review the vendor installation instructions first, prefer a signed or checksum-verified package when available, and require user approval before any CLI install or login step.

## Reference(s):

- [ClawHub Xweather skill page](https://clawhub.ai/oomol/skills/oo-aerisweather)
- [Xweather homepage](https://www.xweather.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; action responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
