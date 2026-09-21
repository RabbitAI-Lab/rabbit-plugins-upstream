## Description:

AbuseIPDB (abuseipdb.com). Use this skill for AbuseIPDB requests that search and read data through the OOMOL-connected AbuseIPDB connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, and operations teams use this skill to query AbuseIPDB for IP reputation, CIDR block reports, detailed IP reports, and blacklist feed data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions can execute a remote oo CLI installer directly in a shell.

Mitigation: Use the official installation guide, verify or pin the installer or package before running it, and invoke setup only when the CLI is missing or authentication/connection errors require it.

## Reference(s):

- [AbuseIPDB homepage](https://www.abuseipdb.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal actions are read-only AbuseIPDB connector calls; setup guidance is used only after authentication, connection, or missing-CLI failures.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
