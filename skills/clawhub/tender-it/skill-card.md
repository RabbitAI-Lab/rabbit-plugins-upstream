## Description:

帮助查询和分析招投标公告、企业信息与市场数据，默认聚焦 IT、信息化和数字化项目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标及市场分析人员可查询中国招投标项目、追踪项目进展，并分析企业中标记录、竞争对手和采购趋势；IT 与信息化是默认检索方向，用户可指定其他范围。

### Deployment Geography for Use:

Global (focused on Chinese tender and company data)

## Known Risks and Mitigations:

Risk: API credentials are sent to zhiliaobiaoxun.com services and may be stored locally in ~/.zlbx/config.json.

Mitigation: Use a dedicated API key, restrict access to the local configuration file, and review service access before enabling the skill.

Risk: Automatic trial registration can collect a hashed MAC address and device characteristics.

Mitigation: Ask for explicit consent before registration and skip registration when the user declines.

Risk: Hidden request identity and update-acknowledgment behavior may be easy to overlook.

Mitigation: Review these behaviors before deployment and request that the publisher expose them in clear configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-it)
- [Publisher profile](https://clawhub.ai/user/bailianai)
- [Service homepage](https://ai.zhiliaobiaoxun.com/?ch=s153)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language answers with lists and tables when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the actual search scope and distinguishes returned records from inference.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
