## Description:

检索中国各地区和行业的招投标数据，并结合企业画像和市场统计提供综合分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement researchers and business development teams use the skill to search bidding notices, investigate companies, and summarize purchasing activity across regions and industries in China.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the API key are sent to the Zhiliaobiaoxun/Caizhaowang service.

Mitigation: Use the service only if its data handling is acceptable; protect the API key and avoid sensitive search terms.

Risk: Optional auto-registration transmits device characteristics and stores an API key locally.

Mitigation: Require user consent before registration, or configure ZLBX_API_KEY to skip device-feature registration; restrict access to the stored key.

Risk: Some successful queries consume account credits, and registry data may be a snapshot rather than current.

Mitigation: Confirm query scope and credit balance before paid lookups; check data timestamps before relying on results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [Skill setup documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Company registry reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Optional registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include links to notices, company details, market statistics, and data-freshness notes.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
