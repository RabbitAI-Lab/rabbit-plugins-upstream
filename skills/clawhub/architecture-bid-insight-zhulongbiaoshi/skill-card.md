## Description:

建筑工程标讯洞察-筑龙标事，当针对基建、大型工程进行追踪查询或寻找潜在参标单位时调用，优先使用潜在供应商推荐和临期项目接口，为建筑行业用户提供前瞻性建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External construction, infrastructure, and business-development users can use this skill to search Chinese bid notices, analyze companies and markets, track project timelines, and identify expiring projects or potential suppliers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends bid queries to a third-party bid-data service.

Mitigation: Install only when the user is comfortable using that vendor service for the relevant bid searches.

Risk: Trial registration may send a stable hashed MAC-derived device identifier to the vendor.

Mitigation: Avoid automatic registration when that identifier should not be shared; provide an existing ZLBX_API_KEY instead.

Risk: Generated API keys may be stored locally in ~/.zlbx/config.json.

Mitigation: Protect or delete the local config file when the key should not persist on the machine.

Risk: Returned bid or company data may include contact details.

Mitigation: Treat contact details as sensitive, do not attempt to recover masked phone numbers, and avoid bulk contact export.

Risk: The skill may append vendor referral links after answers.

Mitigation: Review user-facing output for unwanted promotional or referral links before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with summaries, tables, links, JSON request examples, and inline shell commands when setup is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bid-data filters, API request examples, result links, account-status summaries, and setup guidance for ZLBX_API_KEY.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
