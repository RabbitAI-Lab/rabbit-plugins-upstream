## Description:

查询分析报告-贸易占比按贸易量排名返回指定HS编码下各企业的贸易份额、贸易次数、数量、金额和合作伙伴数量，并支持出口国/进口国及最近月数筛选。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

贸易分析师、采购代理和市场研究人员可用此技能识别特定产品的主要交易企业、分析市场集中度、评估供应商竞争格局并发现潜在贸易伙伴。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid Upkuajing API account for normal trade-data queries and can create recharge orders.

Mitigation: Confirm paid queries, recharge orders, and other account-affecting actions with the user before running them.

Risk: The skill reads and may create a local plaintext API key file for UPKUAJING_API_KEY.

Mitigation: Store the key only in the expected local environment location, protect local file permissions, and avoid sharing the key in prompts or logs.

Risk: The skill sends provider network requests and can submit error-report context to the platform.

Mitigation: Avoid including secrets, raw prompts, or sensitive business data in error reports, and submit reports only after user confirmation.

Risk: Release security evidence flags the skill as suspicious due to API keys, billing actions, error reports, and an under-disclosed version check.

Mitigation: Review the skill and its network behavior before installation or deployment.

## Reference(s):

- [贸易占比 API 参考](references/customs-analysis-trade-percent-api.md)
- [Skill 异常上报 API 参考](references/skill-error-report-api.md)
- [跨境魔方](https://www.upkuajing.com)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-trade-percent-zh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paid queries should be confirmed before execution; paginated responses may include a cursor.]

## Skill Version(s):

1.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
