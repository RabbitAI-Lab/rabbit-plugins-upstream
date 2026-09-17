## Description:

ipstack lets agents use OOMOL's oo CLI connector to look up IPv4 or IPv6 geolocation data through an OOMOL-connected ipstack account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run ipstack geolocation lookups for a single IP address, the requester IP address, or multiple IP addresses without handling raw API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path asks users or agents to run remote installer scripts directly in a shell.

Mitigation: Review the setup path before installation, prefer independently verified OOMOL documentation or a signed/version-pinned package, and do not let an agent automatically run curl-to-bash or irm-to-iex commands.

Risk: Authentication, connection, or billing failures may require account setup outside the normal read-only lookup flow.

Mitigation: Use setup actions only after a matching command failure, keep credentials in OOMOL's connection flow, and avoid retrying billing-blocked requests until the account issue is resolved.

## Reference(s):

- [ClawHub ipstack Skill](https://clawhub.ai/oomol/skills/oo-ipstack)
- [ipstack Homepage](https://ipstack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookup workflow; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
