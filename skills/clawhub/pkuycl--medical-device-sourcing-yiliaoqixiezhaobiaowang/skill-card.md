## Description:

Helps users research Chinese medical-device and consumables procurement by searching tender awards, comparing winning prices and brands, and reviewing purchaser and product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and suppliers use this skill to find medical-device and consumables tenders, compare awarded prices and brands, and review purchasing organizations in China.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: A procurement API key is used for account checks and may be stored locally.

Mitigation: Review account access and local credential storage before installation; protect the API key and limit access to its config file.

Risk: Trial registration collects a MAC-derived device hash and device characteristics.

Mitigation: Require informed consent before registration, or use a manually obtained API key instead.

Risk: Hidden comment-based request and update-ack instructions can affect outgoing requests.

Mitigation: Review the skill and reference files before use in sensitive environments and monitor the requested API calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Skill setup documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](references/api-search.md)
- [Market analysis API reference](references/api-market.md)
- [Account and billing API reference](references/api-account.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available procurement records and account credits; some contact numbers may be masked.]

## Skill Version(s):

1.0.9 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
