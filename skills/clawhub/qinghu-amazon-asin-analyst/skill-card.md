## Description:

青虎AI 亚马逊 ASIN 解析：查单个 ASIN 的基础信息、类目与 BSR、价格与成交价历史、Buy Box 与卖家数变化、评论评分趋势、变体父子关系、FBA 费用与尺寸重量，以及它的流量词与出单词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace analysts use this skill to inspect a specified ASIN or Amazon product link, summarize product health, review price and ranking trends, identify review pain points, and assess follow-on selling or differentiation opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad product or link-analysis phrasing.

Mitigation: Confirm the user intends Amazon ASIN analysis and has provided a specific ASIN or Amazon product link before making API calls.

Risk: Qinghu API calls require a user key and may spend Qinghu credits.

Mitigation: Request user confirmation before calls, use only the user's Qinghu token or configured environment token, and report actual credit use from the API response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-asin-analyst)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with concise conclusions, metric summaries, trend interpretation, and optional exported table file links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Qinghu API tools after user confirmation and may export large returned record sets to files instead of inline tables.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
