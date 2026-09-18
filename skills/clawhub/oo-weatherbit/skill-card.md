## Description:

Weatherbit (weatherbit.io). Use this skill for ANY Weatherbit request - searching and reading data. Whenever a task involves Weatherbit, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current weather observations and daily or hourly forecasts from Weatherbit through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe scripts directly into a shell.

Mitigation: Prefer OOMOL's official install guide or a pinned, verifiable package, and review the installer source before running it.

Risk: Use depends on an OOMOL-connected account for Weatherbit access.

Mitigation: Install only when the user is comfortable using OOMOL's oo CLI and Weatherbit through that connected account.

## Reference(s):

- [Weatherbit homepage](https://www.weatherbit.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Weatherbit skill page](https://clawhub.ai/oomol/skills/oo-weatherbit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the OOMOL oo CLI to inspect Weatherbit action schemas and run read-only weather queries.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
