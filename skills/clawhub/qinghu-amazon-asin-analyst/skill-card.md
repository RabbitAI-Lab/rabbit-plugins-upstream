## Description:

青虎AI 亚马逊 ASIN 解析：查单个 ASIN 的基础信息、类目与 BSR、价格与成交价历史、Buy Box 与卖家数变化、评论评分趋势、变体父子关系、FBA 费用与尺寸重量，以及它的流量词与出单词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators and ecommerce analysts use this skill to inspect a specified ASIN or Amazon product URL, assess product health, review trends, compare traffic and conversion keywords, and decide whether and how to compete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API key and can make paid API calls.

Mitigation: Require user approval before the first tool call, report actual Qinghu point consumption from the response envelope, and use environment variables or user-provided credentials rather than hardcoding secrets.

Risk: Generic competitor-analysis prompts could activate the skill when the user has not supplied a concrete Amazon product.

Mitigation: Invoke it with a specific ASIN or Amazon product URL, and ask for clarification when marketplace or product identity is ambiguous.

Risk: API failures can appear successful if only HTTP 200 or the outer isError flag is checked.

Mitigation: Check protocol errors, result.isError, and the parsed inner JSON code and success values before treating a call as successful.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-asin-analyst)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with concise recommendations, optional exported table files for larger datasets, and JSON or shell examples for API calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should lead with a recommendation, label numeric scope and sample size, avoid dumping large raw datasets into chat, and report Qinghu point consumption when paid calls are made.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
