## Description:

ipdata.co helps agents query ipdata.co through the OOMOL oo CLI for IP geolocation, ASN, carrier, company, currency, timezone, and threat intelligence lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform ipdata.co lookups through an OOMOL-connected account without calling the API directly. It supports single-IP, current-IP, bulk IP, ASN, carrier, company, currency, timezone, and threat intelligence queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup recommends executing downloaded installer scripts for the OOMOL CLI.

Mitigation: Review the setup before installation, prefer a verified or package-manager install path where available, and avoid administrator privileges.

Risk: IP addresses and current-IP lookups may be sent through OOMOL to ipdata.co.

Mitigation: Confirm that the requested lookup data is appropriate to send through the connected services before running commands.

## Reference(s):

- [ipdata.co homepage](https://ipdata.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ipdata-co)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; command responses are JSON objects with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
