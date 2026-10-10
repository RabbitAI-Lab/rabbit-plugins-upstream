## Description:

Helps agents discover Penny Press essays for free and access full text through USDC micropayments on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[con-scribe](https://clawhub.ai/user/con-scribe)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and developers use this skill to browse the free essay catalog and obtain full Markdown text for programmatic reading after approving a per-essay payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Programmatic full-text reads may incur USDC charges.

Mitigation: Verify the official endpoint, current price, Base network, USDC asset, and recipient address before approving each payment.

Risk: Wallet credentials could be exposed if shared with an untrusted request.

Mitigation: Never provide private keys or seed phrases; sign only with your own trusted wallet tooling.

## Reference(s):

- [Penny Press](https://www.pennypress.org)
- [Penny Press pricing and payment details](https://www.pennypress.org/.well-known/x402)
- [Penny Press skill on ClawHub](https://clawhub.ai/con-scribe/skills/penny-press)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON catalog and essay responses with Markdown full text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Catalog access is free; programmatic full-text reads require a per-essay USDC payment on Base.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
