## Description:

API Ninjas (api-ninjas.com) connector for searching and reading data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect API Ninjas connector schemas and run read-oriented data lookups for air quality, geocoding, reverse geocoding, timezone, weather, and weather forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions recommend piping remote installer scripts directly into Bash or PowerShell.

Mitigation: Review the oo CLI installation path first and prefer an official package manager, versioned release, or installer with a verifiable signature or SHA-256 digest.

Risk: Connector use depends on an installed, signed-in, and connected oo CLI environment.

Mitigation: Run first-time setup only after a matching command failure and verify the API Ninjas connection before retrying connector reads.

## Reference(s):

- [API Ninjas homepage](https://api-ninjas.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-api-ninjas)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
