## Description:

Kuaidi100 enables agents to query shipment tracking, detect carriers, estimate shipping price and timing, and manage pickup orders through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with OOMOL-connected Kuaidi100 accounts use this skill to inspect connector schemas, build JSON payloads, query logistics data, estimate shipment cost and timing, and manage pickup orders with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes one-line remote installer commands.

Mitigation: Inspect the installer before execution, use a pinned release, or verify a signature or checksum before installing the oo CLI.

Risk: Shipping, order, and logistics data is sent through OOMOL and Kuaidi100.

Mitigation: Install only when the user trusts OOMOL and Kuaidi100 for the relevant shipment and order data.

Risk: Pickup-order actions can create or cancel real orders.

Mitigation: Confirm the exact payload and intended effect with the user before running create_order, cancel_order, order_price, or other state-changing actions.

## Reference(s):

- [Kuaidi100 Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-kuaidi100)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Kuaidi100 Homepage](https://www.kuaidi100.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that return JSON connector responses containing data and meta.executionId.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
