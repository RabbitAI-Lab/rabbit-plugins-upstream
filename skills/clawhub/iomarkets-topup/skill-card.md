## Description:

IoMarkets Topup helps agents quote and buy mobile airtime or data top-ups with USDC on Algorand via x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sergovashakmadze](https://clawhub.ai/user/sergovashakmadze)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to look up mobile operators and offers, quote USDC prices, and complete human-confirmed airtime or data top-ups for supported phone numbers.

### Deployment Geography for Use:

Global, subject to live catalog availability in supported countries.

## Known Risks and Mitigations:

Risk: The skill can initiate paid mobile top-up purchases.

Mitigation: Require explicit human confirmation of the phone number, operator, delivered value, and USDC price before every purchase, and keep a low wallet budget.

Risk: Operator auto-detection can be wrong for MVNO phone numbers, and a voucher bought for the wrong network may be delivered without being redeemable or refundable.

Mitigation: Confirm the operator with the human before buying and use available alternate brand information to correct the selected network.

Risk: Local MCP use can expose wallet-signing capability if the mnemonic is mishandled.

Mitigation: Prefer the hosted MCP when possible; for local signing, store the mnemonic in a protected file and avoid inline secrets in configuration.

Risk: Some product types are supplier-gated or unavailable even if implemented.

Mitigation: Use the live catalog as the authority before offering eSIMs, bills, payouts, or any top-up option to a human.

## Reference(s):

- [IoMarkets homepage](https://iomarkets.app)
- [IoMarkets agent documentation](https://iomarkets.app/agent.md)
- [IoMarkets Topup ClawHub listing](https://clawhub.ai/sergovashakmadze/skills/iomarkets-topup)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown text with HTTP examples and JSON MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include human-confirmation wording, quote and order status details, receipt or refund links, and budget or operator checks.]

## Skill Version(s):

0.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
