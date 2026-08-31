## Description:

青虎AI 小红书社媒运营：结合小红书热搜榜、关键词搜索笔记、笔记内容与评论、达人主页与作品数据，完成「爆款笔记拆解 → 种草痛点提取 → 优质 KOC/KOL 筛选」，搭建高效种草与社媒矩阵方案，并可生成小红书种草码。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External social-media operators and agents use this skill to research Xiaohongshu/Rednote trends, decompose high-performing notes, extract audience pain points, screen KOC/KOL candidates, and plan seeding campaigns. It supports API-assisted data collection and can generate concise strategy deliverables or spreadsheet exports for larger result sets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request or use a Qinghu API token.

Mitigation: Use user-provided authorization or approved environment variables, and avoid exposing tokens in generated outputs.

Risk: Qinghu data calls can consume account credits.

Mitigation: Ask for user confirmation before tool calls, report actual consumption from the response envelope, and stop when authorization is missing or unclear.

Risk: Large research results may create local spreadsheet exports.

Mitigation: Use exports only for larger datasets, keep chat previews short, and include source scope and sample size in conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-rednote-social)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown summaries with optional spreadsheet file exports and inline JSON or shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state data scope and sample size, avoid dumping large raw datasets into chat, and report Qinghu point consumption when paid calls are made.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
