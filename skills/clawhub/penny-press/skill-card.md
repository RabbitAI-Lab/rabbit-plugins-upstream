## Description:

Helps agents discover Penny Press essays and collections, access paid text with USDC micropayments on Base, and use LitWit literary attestations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[con-scribe](https://clawhub.ai/user/con-scribe)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and developers use this skill to find free catalog information, retrieve paid essays and collections, and verify or request literary attestations through Penny Press.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid reads or attestations can spend USDC on Base.

Mitigation: Check the live payment challenge, price, network, asset, and recipient before signing each transaction.

Risk: Sharing wallet credentials could expose funds.

Mitigation: Keep private keys and seed phrases out of the skill and sign only with trusted wallet tooling.

## Reference(s):

- [Penny Press](https://www.pennypress.org)
- [Penny Press payment details](https://www.pennypress.org/.well-known/x402)
- [Penny Press MCP endpoint](https://www.pennypress.org/mcp)
- [Penny Press skill release on ClawHub](https://clawhub.ai/con-scribe/skills/penny-press)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown; service responses may contain JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Catalog lookups and hash verification are free; programmatic full-text reads and attestations may require payment.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
