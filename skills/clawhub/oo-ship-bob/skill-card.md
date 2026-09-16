## Description:

ShipBob helps agents search and read ShipBob inventory, product, channel, and fulfillment-location data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query ShipBob business data from a connected ShipBob account without calling the ShipBob API directly. It is suited for read-only workflows such as reviewing inventory levels, products, channels, and fulfillment locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute arbitrary code.

Mitigation: Install the oo CLI only from a trusted, verified, versioned release or package manager, and do not allow an agent to run remote installer commands unattended.

Risk: Connecting ShipBob exposes business data access through the configured account.

Mitigation: Treat the connector as business-data access, verify the account connection and scopes, and review commands before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ship-bob)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ShipBob Homepage](https://www.shipbob.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on live oo CLI connector schemas and the connected ShipBob account.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
