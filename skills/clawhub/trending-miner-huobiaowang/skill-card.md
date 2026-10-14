## Description:

分析招投标数据，汇总行业热度、主要采购方及近期高频中标记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

采购与市场分析人员可查询中国招投标公告、识别主要采购方和中标方，并分析特定行业的市场热度与集中度。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives credential-linked package details, and automatic registration transmits a hashed MAC-derived device identifier.

Mitigation: Review these data transfers before use; configure your own API key through a trusted credential mechanism to avoid automatic registration.

Risk: An API key may be stored locally in ~/.zlbx/config.json.

Mitigation: Review local credential storage and restrict access to the configuration file.

Risk: Contact lookups and automatic company expansion can expose more information or incur additional usage than expected.

Mitigation: Limit queries to the requested companies and records, verify costs, and do not reconstruct or bulk-export masked contact details.

Risk: The skill includes background account checks and update-notice acknowledgment instructions.

Mitigation: Review network requests and ensure any acknowledgment follows a notice actually shown to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/trending-miner-huobiaowang)
- [Market analysis API reference](references/api-market.md)
- [Search API reference](references/api-search.md)
- [Automatic registration and credential handling](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with links to source notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect the requested filters and available provider data.]

## Skill Version(s):

2.1.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
