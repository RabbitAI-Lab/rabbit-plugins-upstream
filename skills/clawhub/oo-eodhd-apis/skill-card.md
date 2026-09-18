## Description:

EODHD APIs provides an agent interface for retrieving financial market, macroeconomic, account, and reference data from EODHD through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to search EODHD instruments and retrieve market, macroeconomic, Treasury yield, account, and API usage data through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to execute remote installer scripts directly in a shell.

Mitigation: Review the skill before installation, prefer a signed or otherwise verifiable oo CLI release path, and inspect installer contents before execution.

Risk: The skill relies on an authenticated EODHD account connected through OOMOL.

Mitigation: Connect only the EODHD account intended for this skill and stop if authentication, scope, credential expiration, or billing errors occur.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-eodhd-apis)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [EODHD APIs Homepage](https://eodhd.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; credentials are handled by OOMOL and are not exposed to the agent.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
