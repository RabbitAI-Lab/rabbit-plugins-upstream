## Description:

Lingxing enables agents to read, create, and update Lingxing ERP data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Lingxing connector schemas and run oo CLI actions for product, listing, inventory, shipment, seller, marketplace, currency, profitability, and advertising workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review the installer path before installing, prefer official downloads, and verify publisher signatures or checksums where available.

Risk: Some Lingxing actions can change account data.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [Lingxing homepage](https://www.lingxing.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lingxing)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and can return JSON connector responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
