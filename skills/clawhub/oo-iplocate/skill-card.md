## Description:

IPLocate lets agents query IPLocate geolocation, ASN, privacy, hosting, company, and abuse data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up IPLocate data for one IP address, multiple IP addresses, or the connector server's outgoing IP address while relying on OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include one-line remote installer commands that execute directly in a shell.

Mitigation: Prefer a trusted package source, or download, inspect, and verify the installer before executing it.

## Reference(s):

- [ClawHub IPLocate Skill Page](https://clawhub.ai/oomol/skills/oo-iplocate)
- [IPLocate Homepage](https://www.iplocate.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI command examples and JSON payload and response expectations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live connector schema before running IPLocate actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
