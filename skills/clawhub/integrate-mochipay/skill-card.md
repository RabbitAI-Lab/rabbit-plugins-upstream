## Description:

Guides developers in integrating MochiPay crypto checkout into stores, backends, and mobile apps with verified payment states and callbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and merchants use this skill to install or repair MochiPay checkout integrations, select supported store packages, and implement authenticated payment verification and once-only fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Store or payment-code changes can affect live checkout and order fulfillment.

Mitigation: Review changes and explicitly approve live orders, credential changes, deployments, and production payment enablement.

Risk: Payment credentials and wallet secrets could be exposed during integration.

Mitigation: Keep API keys, wallet secrets, recovery phrases, and private configuration out of chat.

Risk: Installing an unverified gateway ZIP could introduce unwanted code.

Mitigation: Verify download domains and package hashes before installation.

## Reference(s):

- [MochiPay Integration skill release](https://clawhub.ai/hznetnewpower/skills/integrate-mochipay)
- [MochiPay developer skill documentation](https://mochi.bz/Developers/Skill.aspx)
- [MochiPay API reference](https://mochi.bz/Developers/Reference.aspx)
- [API integration contract](references/api-integration.md)
- [Store packages](references/store-packages.md)
- [Returns and notifications](references/returns-notifications.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include integration checks, changed files, and outstanding verification steps.]

## Skill Version(s):

1.2.14 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
