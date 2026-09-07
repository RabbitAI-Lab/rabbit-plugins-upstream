## Description:

热门标讯挖掘助手-火标网，当用户需要进行行业热度分析、统计Top采购商或聚合近期高频中标记录时调用，调用多维度聚合统计接口，呈现特定行业的市场热度与集中度趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Chinese tender and award data, identify active purchasers and suppliers, and summarize market concentration or heat by industry, keyword, region, amount, and time window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate provider onboarding with a persistent device fingerprint when no API key is configured.

Mitigation: Configure ZLBX_API_KEY manually when possible, and allow automatic registration only after reviewing and accepting the stated device data collection.

Risk: The skill may store a service API key in ~/.zlbx/config.json.

Mitigation: Review local file permissions and avoid sharing the generated configuration file or API key.

Risk: The skill accesses procurement records, contact data, and provider-hosted services.

Mitigation: Confirm the provider's terms and data handling expectations before using the skill with sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/trending-miner-huobiaowang)
- [ClawHub publisher profile](https://clawhub.ai/user/liu-jiapeng)
- [Search tender API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account query API reference](artifact/references/api-account.md)
- [Automatic registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, JSON API request examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an approved onboarding flow before data API calls.]

## Skill Version(s):

2.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
