## Description:

Provides agent access to Ipregistry lookups through OOMOL's oo CLI connector for IP, ASN, and user-agent queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to run Ipregistry connector actions for IP geolocation, ASN lookup, and user-agent parsing through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes commands that execute remotely downloaded installer scripts.

Mitigation: Use an official packaged or otherwise verifiable oo CLI install path, inspect installer contents, and avoid letting an agent run the remote installer automatically.

Risk: Connector lookups disclose queried IP addresses, ASNs, or user-agent strings to the connected service.

Mitigation: Confirm the data is appropriate to send to Ipregistry before running lookup or parsing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ipregistry)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Ipregistry Homepage](https://ipregistry.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON-formatted connector responses from Ipregistry actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
