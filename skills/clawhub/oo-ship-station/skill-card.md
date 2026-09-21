## Description:

ShipStation helps agents inspect connector schemas and retrieve ShipStation purchase order and inventory data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read ShipStation purchase orders, inventory levels, and inventory warehouses from a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that run directly in a shell.

Mitigation: Prefer official install documentation and checksum or signature verification where available before running installer commands.

Risk: ShipStation data is routed through OOMOL's connector.

Mitigation: Install only when the user trusts OOMOL and is comfortable with that data path.

Risk: The security summary notes that the action scope is broader than the read-only description.

Mitigation: Inspect the live action schema before each request and get explicit user approval before any setup or non-read action.

## Reference(s):

- [ClawHub ShipStation skill page](https://clawhub.ai/oomol/skills/oo-ship-station)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ShipStation homepage](https://www.shipstation.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; read actions return ShipStation data when credentials are connected.]

## Skill Version(s):

1.0.3 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
