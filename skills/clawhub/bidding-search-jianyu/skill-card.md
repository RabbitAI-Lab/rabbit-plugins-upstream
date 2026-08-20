## Description:

招中标信息&招标雷达 helps agents search and analyze Jianyu/Zhiliaobiaoxun tender and bid data for opportunities, expiring projects, company activity, suppliers, brands, prices, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, procurement analysts, and agents use this skill to retrieve bid and tender announcements, company profiles, competitor and partner information, account status, and market aggregates from the Zhiliaobiaoxun/Jianyu data service. It supports opportunity tracking, supplier discovery, historical price review, and procurement market analysis.

### Deployment Geography for Use:

Global, with China-focused tender and company data.

## Known Risks and Mitigations:

Risk: The security review reports under-disclosed account setup that can derive a stable device identifier, send it to a vendor service, and save an API key locally.

Mitigation: Review the skill before installation, prefer manually creating and supplying ZLBX_API_KEY, and confirm consent before any automatic account setup.

Risk: The skill can guide agents toward contact-data queries and vendor recharge or login links.

Mitigation: Use contact-data queries only for legitimate business needs and verify account or recharge links before acting on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liu-jiapeng/skills/bidding-search-jianyu)
- [Skill Definition](artifact/SKILL.md)
- [Search API Reference](artifact/references/api-search.md)
- [Company API Reference](artifact/references/api-company.md)
- [Market API Reference](artifact/references/api-market.md)
- [Account API Reference](artifact/references/api-account.md)
- [Automatic Registration Reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with tables or charts, plus JSON/API examples and shell commands when setup or account checks are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a configured vendor account; service responses may include bid, company, account, and market data.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
