## Description:

Operate ShipStation through an OOMOL-connected account to retrieve purchase orders and list inventory, warehouses, and purchase orders via the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ShipStation through an OOMOL-connected account, inspect live action schemas, retrieve purchase orders, and list inventory and warehouse data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer snippets that could execute unverified code if run automatically.

Mitigation: Do not let an agent run the remote installer snippets automatically; install the oo CLI only through a verified official method, preferably with a pinned release and checksum or signature verification.

Risk: Some ShipStation actions may change account state when invoked with an incorrect payload.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running any action tagged as write or destructive.

## Reference(s):

- [ShipStation skill page](https://clawhub.ai/oomol/skills/oo-ship-station)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ShipStation homepage](https://www.shipstation.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON data]

**Output Format:** [Markdown guidance with bash and PowerShell command examples plus JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; first-time setup is only used after authentication or connection failures.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
