## Description:

Guides developers through validating an external x402 service and listing it in the Nevermined Agent Services Catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers use this skill to check whether an external x402 service can be paid directly, publish and promote it in the Nevermined Catalog, and verify a paid call through the Nevermined Router.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial and does not establish that the skill is safe; the skill also sends requests to external services and includes an executable payment helper.

Mitigation: Review the skill and helper before execution, confirm that the external services are trusted, and grant shell access only when needed.

Risk: Direct-wallet validation can authorize a real USDC payment using a private key and a merchant-provided payment challenge.

Mitigation: Use a throwaway EOA funded only for the test, keep the helper's asset and amount checks enabled, and never expose the private key.

## Reference(s):

- [Nevermined Catalog overview](https://nevermined.ai/docs/products/catalog/overview)
- [Nevermined Catalog Onboarding on ClawHub](https://clawhub.ai/nevermined-io/skills/nevermined-catalog-onboarding)
- [Claiming listings and using credits](references/claim-and-credits.md)
- [Direct wallet payment guide](references/direct-wallet-pay.md)
- [Catalog listing and promotion guide](references/list-and-promote.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline shell commands, JSON examples, and JavaScript code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes workflow steps, API request examples, and validation criteria.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
