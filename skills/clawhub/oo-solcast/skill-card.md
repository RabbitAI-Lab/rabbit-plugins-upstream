## Description:

Operates Solcast through OOMOL's oo CLI to retrieve irradiance and weather forecast, historical, and live estimated actuals data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Solcast irradiance and weather forecasts, historical estimated actuals, and live estimated actuals by coordinates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents curl-to-bash and PowerShell pipe-to-iex installer commands that can execute remote code locally.

Mitigation: Review before installing; use the remote installer only if OOMOL's installer source is independently trusted, and prefer a pinned, signed, or package-manager install path when available.

## Reference(s):

- [ClawHub Solcast Skill](https://clawhub.ai/oomol/skills/oo-solcast)
- [Solcast Homepage](https://solcast.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload and response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; Solcast credentials are managed server-side by OOMOL.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
