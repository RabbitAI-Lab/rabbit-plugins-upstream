## Description:

Helps construction-sector users find and track Chinese infrastructure tenders, approaching project deadlines, and potential bidders and suppliers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Construction-industry professionals use this skill to search Chinese tender and award records, track large projects, identify potential suppliers, and spot upcoming opportunities. It queries the Zhiliaobiaoxun service using an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives API requests authenticated with an API key, which automatic registration may save locally.

Mitigation: Review the provider's access terms and local key storage before use; set ZLBX_API_KEY manually if you prefer not to auto-register.

Risk: Automatic registration collects a hashed device identifier for account creation.

Mitigation: Require informed consent before collecting device attributes or registering; decline registration if this is unsuitable.

Risk: Hidden comment blocks contain request and update-acknowledgment behavior that may be overlooked.

Mitigation: Review the full skill text and account/update acknowledgment behavior before enabling it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Registration and credential guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown summaries with source links and bid data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available API records and account quota.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
