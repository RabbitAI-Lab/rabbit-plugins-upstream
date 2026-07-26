## Description: <br>
中标结果查询与竞争分析服务，用于查询中标公告与中标单位、企业招中标战绩画像、竞争对手识别与重叠度分析、Top中标单位/中标品牌统计、历史中标价格走势。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, procurement teams, and competitive analysts use this skill to find bid-award outcomes, profile bidders and suppliers, identify overlapping competitors, and review pricing or market trends from bid data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can silently collect device and local user identifiers, create a remote account, store an API key, and generate login or recharge links. <br>
Mitigation: Review before installing, prefer a user-provided ZLBX_API_KEY, and only allow auto-registration when the user accepts the provider account creation and local credential storage behavior. <br>
Risk: Bid contacts and company data returned by the APIs may include personal or business-sensitive information. <br>
Mitigation: Use returned contact and procurement data only for authorized work, and avoid redistributing sensitive details beyond the intended business workflow. <br>


## Reference(s): <br>
- [标讯搜索类工具 API 详情](references/api-search.md) <br>
- [企业分析类工具 API 详情](references/api-company.md) <br>
- [市场分析类工具 API 详情](references/api-market.md) <br>
- [SKILL 自动注册详细流程](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON request and response examples, shell command snippets, and API-derived analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read ZLBX_API_KEY or ~/.zlbx/config.json, and may store an issued API key under ~/.zlbx/config.json when auto-registration is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
