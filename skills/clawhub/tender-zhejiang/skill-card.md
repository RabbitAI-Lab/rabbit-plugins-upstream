## Description:

查询和分析招投标公告、企业工商资料及采购市场数据，默认聚焦浙江省，也支持用户指定其他地区。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bidding teams use this skill to find tenders and awards, track project stages, research companies and competitors, and compare purchasing trends. Searches default to Zhejiang Province unless the user specifies another region.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no API key is configured, registration can collect device features including a hashed MAC address, create an account, and save a new API key locally.

Mitigation: Review the provider's account flow and obtain consent before registration; prefer a separately configured API key through the host's secret mechanism.

Risk: Some data lookups consume account credits.

Mitigation: Check usage and credit costs before querying; limit requests to the user's requested scope and avoid unnecessary pagination.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bailianai/skills/tender-zhejiang)
- [Provider homepage](https://ai.zhiliaobiaoxun.com/?ch=s152)
- [Bid search reference](artifact/references/api-search.md)
- [Company and registration references](artifact/references/api-company.md)
- [Account and usage reference](artifact/references/api-account.md)
- [Automatic registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with links to source announcements]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results depend on the selected region, filters, available provider data, and account credits.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
