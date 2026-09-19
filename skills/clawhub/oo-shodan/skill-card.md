## Description:

Shodan is an agent skill for searching and reading Shodan data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security practitioners, and external users use this skill to run Shodan searches and lookups, including host search counts, IP host details, domain information, hostname resolution, reverse DNS, and API account details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions ask users to run remote installer scripts directly in a shell.

Mitigation: Install only after trusting OOMOL's installer endpoint, or use a reviewed, version-pinned oo CLI installation path with checksum or signature verification.

Risk: The skill depends on OOMOL-managed credentials for Shodan access.

Mitigation: Confirm the OOMOL account and Shodan connection are appropriate for the user or organization before running lookups.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shodan)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Shodan homepage](https://www.shodan.io)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution and returns Shodan connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
