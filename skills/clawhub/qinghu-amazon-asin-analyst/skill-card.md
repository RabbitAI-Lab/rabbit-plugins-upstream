## Description:

青虎AI 亚马逊 ASIN 解析：查单个 ASIN 的基础信息、类目与 BSR、价格与成交价历史、Buy Box 与卖家数变化、评论评分趋势、变体父子关系、FBA 费用与尺寸重量，以及它的流量词与出单词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace analysts use this skill to evaluate a specified ASIN or Amazon product link, review product status and trends, inspect reviews and traffic keywords, and decide whether and how to compete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API token supplied by the user or environment.

Mitigation: Install only when Qinghu API use is intended, scope token access appropriately, and avoid sharing token values in prompts or exported files.

Risk: Some Qinghu tool calls may consume paid Qinghu points.

Mitigation: Confirm authorization before paid calls and report point consumption using the response envelope value.

Risk: Larger result sets may be cached or exported to local files.

Mitigation: Review generated files before sharing them and remove local exports when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-asin-analyst)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with optional exported local files and inline code or shell commands for API calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include concise previews, file links for larger datasets, and Qinghu point-consumption notes when paid calls are made.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
