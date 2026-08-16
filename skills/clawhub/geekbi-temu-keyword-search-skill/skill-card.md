## Description:

使用极鲸云查询和分析 Temu 关键词数据，帮助用户研究搜索需求、销量与销售额趋势、供给与竞争强度、平均价格、市场时间、类目归属和关键词机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query GeekBI Temu keyword data and compare demand, growth, supply, competition, price, market timing, and category signals for keyword research. It is aimed at Chinese-language cross-border commerce workflows that need concise, evidence-based keyword opportunity analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reuses GeekBI login state across local locations and related Temu skills.

Mitigation: Use it only in workspaces where a local .geekbi/agent-auth.json file is acceptable, and clear the stored auth state when shared session reuse is no longer desired.

Risk: Queries can pause when the GeekBI service requires login, quota, recharge, access, or rate-limit action before data is available.

Mitigation: Show only the server-provided user-facing prompt and jump link, pause analysis until the user completes the action, then rerun the same query.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/geekbi/geekbi-temu-keyword-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-keyword-search-skill)
- [Temu 关键词搜索](references/Temu关键词搜索.md)
- [Temu 关键词搜索接口](references/Temu关键词搜索接口.md)
- [Temu 关键词榜单预设](references/Temu关键词榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses with keyword links, concise conclusions, data scope, analysis tables or lists, and follow-up validation guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Helper scripts return JSON for successful API responses or action-required pause states; user-facing answers should hide raw implementation details unless requested.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
