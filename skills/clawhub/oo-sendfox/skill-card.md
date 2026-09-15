## Description:

Operates SendFox through the OOMOL-connected oo CLI for reading, creating, updating, and deleting contacts and contact lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage SendFox contacts, contact lists, memberships, searches, custom fields, and unsubscribe state through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts directly from the network.

Mitigation: Review the OOMOL CLI installer through a safer download-and-verify flow before running it.

Risk: Write and destructive SendFox actions can modify, remove, or unsubscribe contacts and lists.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before executing state-changing commands.

Risk: The connector should only be used for SendFox tasks after authentication and account connection are in place.

Mitigation: Limit use to SendFox requests and follow setup guidance only after an auth, connection, or missing-command failure.

## Reference(s):

- [SendFox homepage](https://sendfox.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing SendFox action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
