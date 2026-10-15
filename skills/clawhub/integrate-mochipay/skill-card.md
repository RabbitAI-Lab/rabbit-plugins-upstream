## Description:

Guides authorized MochiPay crypto-payment integration for stores, backends, and mobile apps, including checkout modes, notifications, retries, and verified payment states.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and merchants use this skill to select compatible MochiPay packages or implement and repair authorized crypto-payment checkout integrations, while verifying payment status before fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing API keys, wallet credentials, or recovery phrases during integration work.

Mitigation: Keep secrets out of chat and client code; enter merchant credentials privately on the server.

Risk: Installing an incorrect or unverified payment package.

Mitigation: Check platform and runtime compatibility, and verify official package downloads and hashes before installation.

Risk: Fulfilling orders based on unverified payment or duplicate notifications.

Mitigation: Re-query the authenticated API, confirm the saved order and amount bindings, and fulfill at most once.

Risk: Unapproved changes to live payments or merchant configuration.

Mitigation: Require explicit merchant approval before deployment, live-order creation, credential rotation, or fulfillment changes.

## Reference(s):

- [MochiPay integration skill](https://mochi.bz/Developers/Skill.aspx)
- [MochiPay developer reference](https://mochi.bz/Developers/Reference.aspx)
- [API integration contract](references/api-integration.md)
- [Store package compatibility](references/store-packages.md)
- [Returns and notifications](references/returns-notifications.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration changes require merchant authorization and independent payment verification.]

## Skill Version(s):

1.2.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
