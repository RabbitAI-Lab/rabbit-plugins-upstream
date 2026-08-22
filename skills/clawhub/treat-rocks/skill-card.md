## Description:

Buy a novelty digital rock from treat.rocks over x402 (USDC on Base): a signed, independently verifiable certificate for your agent at a fixed price, with no token and no investment claim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smelly-lemon](https://clawhub.ai/user/smelly-lemon)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through buying and verifying a $2 USDC novelty digital rock from treat.rocks using either MCP-provided payment instructions or direct x402 payment flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides a real USDC purchase on Base, and minted rocks are described as non-refundable.

Mitigation: Confirm the x402 payment details in the user's own wallet or client before signing, including price, network, recipient, asset, and gas.

Risk: The treat.rocks server is closed-source and returns the purchased rock certificate.

Mitigation: Use the verification endpoint after purchase and compare against the published certificate public key when stronger assurance is needed.

Risk: Users could mistake the novelty digital rock for an investment or tokenized asset.

Mitigation: Present it as a fixed-price novelty purchase with no token, no resale market, no subscription, and no investment claim.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smelly-lemon/skills/treat-rocks)
- [treat.rocks homepage](https://treat.rocks)
- [x402 protocol](https://www.x402.org/)
- [treat.rocks store manifest](https://treat.rocks/store.json)
- [treat.rocks x402 discovery manifest](https://treat.rocks/.well-known/x402.json)
- [treat.rocks security posture](https://treat.rocks/SECURITY.md)
- [treat.rocks certificate public key](https://treat.rocks/.well-known/treatrocks-pubkey.json)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown]

**Output Format:** [Markdown guidance with endpoint URLs and example HTTP interactions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent should surface live payment requirements from treat.rocks or the user's x402 client rather than hardcoding payment details.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
