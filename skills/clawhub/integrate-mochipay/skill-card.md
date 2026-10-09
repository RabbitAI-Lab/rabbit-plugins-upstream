## Description:

Guides authorized MochiPay crypto payment integrations for stores, backends, and mobile apps, including checkout, payment verification, and retry handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and store operators use this skill to install or repair MochiPay checkout in authorized stores and applications, and to implement verified payment updates without exposing merchant credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing payment credentials or customer data during setup.

Mitigation: Enter secrets only in the merchant's backend or dashboard; keep them and private configs out of chat.

Risk: Unverified payments or duplicate fulfillment after returns, callbacks, or retries.

Mitigation: Verify saved order details and paid status through authenticated queries, then fulfill atomically once.

Risk: Incorrect packages or unchecked examples could disrupt a live store.

Mitigation: Use only authorized environments; verify official downloads and compatibility, test callback handling, and validate production payments before launch.

## Reference(s):

- [MochiPay Integration on ClawHub](https://clawhub.ai/hznetnewpower/skills/integrate-mochipay)
- [MochiPay API reference](https://mochi.bz/Developers/Reference.aspx#checkout-modes)
- [MochiPay integration guide](https://mochi.bz/Developers/Skill.aspx)
- [Store packages](references/store-packages.md)
- [Returns and notifications](references/returns-notifications.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration guidance requires merchant-specific compatibility and payment verification.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
