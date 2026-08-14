## Description:

Retrieves translated Zhihuiya/PatSnap patent description text in Chinese, English, or Japanese by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent-focused agents use this skill to retrieve translated patent specification text for known patent IDs or publication numbers. It supports single or batch lookups and can optionally fall back to a patent family member when the requested description is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes account, credential, and SMS-code flows for LinkFox authentication.

Mitigation: Use onboarding commands only when the user intends to create or access a LinkFox account, and avoid sharing SMS codes or API keys outside the configured environment variables.

Risk: The skill can guide paid credit purchases and render payment QR codes.

Mitigation: Confirm plan details, payment method, price, and destination endpoint with the user before creating or paying an order.

Risk: Patent lookup calls consume credits, and batch requests may consume credits quickly.

Mitigation: Warn the user before paid or repeated queries, respect the documented cache behavior, and avoid automatic retries or broad follow-up searches without user approval.

Risk: Full API responses are persisted locally and may contain patent query results or account-related metadata.

Mitigation: Review saved files before sharing the workspace and remove response files when the data is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data-translated)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [Zhihuiya description translation endpoint](https://tool-gateway.linkfox.com/zhihuiya/descriptionDataTranslated)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The main script caches identical requests for 24 hours, saves full responses under a local linkfox session directory, prints small responses inline, and summarizes large responses unless --inline is used.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
