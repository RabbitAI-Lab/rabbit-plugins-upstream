## Description:

Operate Walmart Marketplace through an OOMOL-connected oo CLI connector to read seller catalog, inventory, and order data and update inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketplace operators use this skill to inspect Walmart Marketplace action schemas, retrieve seller items, inventory, and purchase orders, and update inventory through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute directly in a shell.

Mitigation: Review the installer commands before running them and prefer a verified package or downloaded installer that can be inspected.

Risk: Connector actions can affect a live Walmart Marketplace seller account, including inventory changes.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Walmart Marketplace Skill](https://clawhub.ai/oomol/skills/oo-walmart-marketplace)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Walmart Marketplace](https://marketplace.walmart.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and connector JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId when actions run.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
