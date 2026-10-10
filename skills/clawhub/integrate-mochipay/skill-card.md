## Description:

Guides authorized merchants and developers through MochiPay crypto payment integration for stores, backends, and mobile apps, including checkout, callbacks, retries, and verified payment states.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and developers use this skill to select compatible MochiPay packages or implement authorized payment flows in existing stores, backends, and mobile apps. It guides checkout setup, secure status verification, and integration repairs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized changes to a merchant's payment configuration or live checkout.

Mitigation: Work only on authorized stores and backends; obtain explicit approval before live orders, production payment enablement, or deployment.

Risk: Exposure of API secrets, recovery phrases, or customer data.

Mitigation: Keep sensitive values out of chat and enter private settings directly in the merchant system.

Risk: Installing an unverified payment plugin.

Mitigation: Verify official download links and SHA-256 hashes before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hznetnewpower/skills/integrate-mochipay)
- [MochiPay API integration contract](references/api-integration.md)
- [MochiPay store packages](references/store-packages.md)
- [Payment recovery](references/payment-recovery.md)
- [Returns and notifications](references/returns-notifications.md)
- [MochiPay developer API guide](https://mochi.bz/Developers/APIGuide.aspx)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend an optional read-only offline configuration check.]

## Skill Version(s):

1.2.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
