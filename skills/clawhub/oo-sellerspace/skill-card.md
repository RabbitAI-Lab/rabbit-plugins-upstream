## Description:

SellerSpace helps agents query SellerSpace data through the OOMOL oo CLI connector for authorized Amazon stores, marketplace performance, products, shipments, and advertising.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators, e-commerce analysts, and support agents use this skill to retrieve SellerSpace sales, profit, advertising, product, shipment, and store data for authorized Amazon stores. It is suited for read-oriented reporting, troubleshooting, and performance analysis through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive SellerSpace business data, including sales, profit, advertising, shipment, and store identifiers.

Mitigation: Install and use it only for accounts where the agent is allowed to query that data, and limit prompts and outputs to the business context needed for the task.

Risk: Broad trigger wording may cause agents to route any SellerSpace-related request through the connector.

Mitigation: Review the request before execution and use live schema discovery so each connector call is limited to the intended read action and payload.

Risk: Future connector actions could include write or destructive behavior even though the current disclosed release is read-oriented.

Mitigation: Require explicit user confirmation for any action tagged write or destructive, including the exact target, payload, and expected effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sellerspace)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [SellerSpace homepage](https://www.sellerspace.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include SellerSpace query results, schema-informed payload guidance, and first-time setup instructions when authentication or connector setup fails.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
