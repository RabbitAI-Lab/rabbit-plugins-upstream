## Description:

Shopee (shopee.com) support for reading, creating, updating, and deleting Shopee data through the OOMOL-connected Shopee connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to let an agent inspect Shopee merchant, shop, product, inventory, order, return, shipping, tracking, and escrow data, and to perform approved product and fulfillment actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform real Shopee account-changing actions, including shipping, stock, price, and product operations.

Mitigation: Review the exact payload and expected effect before approving any write, shipping, stock, price, or product action.

Risk: The skill depends on the oo CLI and OOMOL account connection for access to Shopee data.

Mitigation: Install only if OOMOL is trusted for the intended account, and verify the oo CLI installer through OOMOL's official documentation before running remote install commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shopee)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Shopee Homepage](https://www.shopee.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
