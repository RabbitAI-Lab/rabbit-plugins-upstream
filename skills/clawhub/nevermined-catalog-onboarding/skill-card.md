## Description:

Guides developers through validating an external x402 service, publishing it in the Nevermined Agent Services Catalog, and confirming paid access through the Router.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and service operators use this skill to determine whether an external x402 service can be listed, validate its payment flow, publish or claim a catalog listing, and test a paid call through Nevermined.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the release suspicious with medium confidence and reports concerns about data disclosure and undeclared capabilities; analysis covered only part of the components.

Mitigation: Review the skill's external requests and tool scope before use, and avoid sending sensitive financial or personal information in requests.

Risk: Direct-wallet validation signs a payment authorization based on a merchant-provided x402 challenge and can spend real funds.

Mitigation: Use a narrowly funded test wallet, check the asset and payment amount, and keep the configured spend cap in place.

Risk: The Nevermined API key and optional wallet private key grant access to sensitive account or payment actions.

Mitigation: Supply secrets through environment variables, never print or share the wallet key, and choose the sandbox environment when testing without real funds.

## Reference(s):

- [Nevermined Catalog overview](https://nevermined.ai/docs/products/catalog/overview)
- [Paying catalog listings with subscription credits](https://nevermined.ai/docs/products/catalog/router/subscription)
- [Direct-wallet payment guide](references/direct-wallet-pay.md)
- [Catalog listing and promotion guide](references/list-and-promote.md)
- [Claiming listings and using credits](references/claim-and-credits.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration instructions]

**Output Format:** [Markdown with inline shell commands, API examples, and JavaScript code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
