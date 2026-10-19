## Description:

Drafts customer-service replies and presales FAQs from supplied product information or supported Douyin and Xiaohongshu product details, while listing facts the merchant still needs to verify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and customer-support staff use this skill to draft buyer replies, presales FAQs, and after-sales explanations from verified product facts and store policies. It separates buyer-facing text from details requiring merchant confirmation and does not send messages or process orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live product lookups invoke an unpinned external npm package with a SocialDataX API key.

Mitigation: Use a reviewed pinned package version or trusted preinstalled CLI, and constrain shell and network access before providing the API key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-customer-service)
- [SocialDataX product information and API key](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Short buyer-facing reply drafts and separate merchant verification lists; structured FAQs when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Douyin and Xiaohongshu product-detail lookups require a SocialDataX API key; supplied product information can be used without one. No automatic messaging or after-sales actions.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
