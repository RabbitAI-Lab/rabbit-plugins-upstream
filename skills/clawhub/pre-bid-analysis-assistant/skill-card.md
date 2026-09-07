## Description:

标前分析助手帮助投标团队在投标前基于知了标讯数据分析项目画像、采购方历史、竞争格局、价格基准、废标风险和投标建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to decide whether to pursue a specific bid, how to price it, which competitors may appear, and what risks need review before submitting. The skill is intended for pre-bid due diligence using vendor-hosted procurement data and user-provided bid details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic vendor account creation may transmit a hashed device identifier and create an account with the data provider.

Mitigation: Set ZLBX_API_KEY manually before use to avoid auto-registration, and review the registration prompt before consenting.

Risk: The skill may store an API key in a local JSON configuration file.

Mitigation: Prefer an environment variable for credentials, restrict local file access, and rotate the key if it may have been exposed.

Risk: Generated HTML reports are active browser files and may contain vendor links and bid-specific data.

Mitigation: Review the report before sharing, open it in a trusted browser context, and avoid distributing reports that contain sensitive bid details.

Risk: Procurement analysis can be incomplete or misleading when public data is missing, stale, or ambiguous.

Mitigation: Require data-gap notes, citations, and human review before using the output for commercial bid decisions.

Risk: API calls consume account credits and may reveal project names, company names, and search terms to the vendor service.

Mitigation: Tell users the expected credit cost before analysis and avoid sending unnecessary confidential query terms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dragonzu/skills/pre-bid-analysis-assistant)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](references/api-quick.md)
- [Bid analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [ZhiLiaoBiaoXun API](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiaoBiaoXun skill docs](https://ai.zhiliaobiaoxun.com/docs/skill)
- [ZhiLiaoBiaoXun business intelligence portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include data gaps, citation details, estimated API-credit consumption, and decision guidance.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
