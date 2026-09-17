## Description:

IP2Location.io lets agents use OOMOL's IP2Location connector to look up IP geolocation, domain WHOIS, and hosted-domain data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run IP2Location.io read-only lookups through an OOMOL-connected account for IP, domain, and network enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer one-liners for the oo CLI.

Mitigation: Review OOMOL's installer source and installation documentation before running the installer, avoid elevated terminals, and prefer a verified package-manager path when available.

Risk: The skill depends on an authenticated OOMOL account and a connected IP2Location.io API key.

Mitigation: Run connection or login setup only after an auth or connection failure, and confirm the account connection before retrying lookups.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ip2location)
- [IP2Location.io Homepage](https://www.ip2location.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before payload construction; credentials are handled by OOMOL.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
