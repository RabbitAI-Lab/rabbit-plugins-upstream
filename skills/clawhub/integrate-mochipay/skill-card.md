## Description:

Guides developers through MochiPay crypto payment integration for stores, backends and mobile apps, including checkout, callbacks, retries and verified fulfillment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and merchants use this skill to select compatible MochiPay packages or adapt an existing application for crypto checkout, authenticated payment verification and safe order fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment credentials or private wallet configuration could be exposed in chat or application output.

Mitigation: Keep API keys, account credentials and private wallet configuration out of chat and retain API secrets on the merchant backend.

Risk: An unverified or mismatched payment could cause incorrect fulfillment.

Mitigation: Verify payment through an authenticated server query and bind the result to the saved order before fulfilling once.

Risk: Downloaded payment packages could be tampered with or incompatible.

Mitigation: Check the provided package hashes and confirm platform and version compatibility before installation.

Risk: Live payment or deployment changes could affect real customer orders.

Mitigation: Require explicit merchant authorization before creating live orders, deploying changes or modifying production payment flows.

## Reference(s):

- [MochiPay Integration on ClawHub](https://clawhub.ai/hznetnewpower/skills/integrate-mochipay)
- [MochiPay integration guide](https://mochi.bz/Developers/Skill.aspx)
- [MochiPay developer reference](https://mochi.bz/Developers/Reference.aspx)
- [Store package compatibility](references/store-packages.md)
- [API integration contract](references/api-integration.md)
- [Payment returns and notifications](references/returns-notifications.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with code and commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the merchant's platform, versions and authorized access.]

## Skill Version(s):

1.2.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
