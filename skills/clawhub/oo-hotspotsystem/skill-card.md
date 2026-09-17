## Description:

HotspotSystem helps agents search and read HotspotSystem owner, customer, subscriber, and location data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and HotspotSystem operators use this skill to inspect live connector schemas and run read-only HotspotSystem actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes shell commands that execute mutable remote installer scripts.

Mitigation: Do not let an agent run the installer commands automatically; install the oo CLI manually from a verified release or package source.

Risk: The connector can read HotspotSystem account data through connected credentials.

Mitigation: Connect only the HotspotSystem account and scopes intended for agent access, and inspect the live action schema before sending payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hotspotsystem)
- [HotspotSystem homepage](https://www.hotspotsystem.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
