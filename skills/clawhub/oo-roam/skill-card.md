## Description:

Roam HQ (ro.am) enables an agent to read, create, and update Roam HQ data through OOMOL's oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Roam HQ through an OOMOL-connected account, including listing groups, magicasts, and recordings and sending group messages with user confirmation for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute code from the network.

Mitigation: Use the skill only if OOMOL and the oo CLI are trusted, and prefer a verified installer or checksum/signature workflow before installation.

Risk: The send_message action can post to a Roam HQ group through the connected account.

Mitigation: Confirm the exact group target, message payload, and expected effect with the user before running write actions.

Risk: Connector behavior depends on the authenticated OOMOL account, active Roam HQ connection, and live action schema.

Mitigation: Fetch the live action schema before submitting payloads and resolve authentication, connection, scope, or billing errors before retrying.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Roam HQ homepage](https://ro.am)
- [Roam HQ connection settings](https://console.oomol.com/app-connections?provider=roam)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before building action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
