## Description:

青虎AI 亚马逊关键词选品：从买家真实搜索词出发做「以词定款」——挖掘高搜索量、低商品供给的蓝海词，验证需求趋势，再反查这些词的流量流向哪些 ASIN，找出纯自然搜索驱动的机会单品。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace sellers, product researchers, and ecommerce operators use this skill to identify keyword-led product opportunities, validate search demand, and inspect which ASINs capture traffic for selected terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Qinghu token, call an external API, and consume Qinghu credits.

Mitigation: Require user confirmation before Qinghu tool calls, report actual credit consumption from the response envelope, and avoid using the skill for generic keyword brainstorming outside its Amazon workflow.

Risk: The workflow depends on external API availability, authentication, and account permissions.

Mitigation: Use the documented authorization header, retry the known intermittent empty 401 case once, and distinguish missing credentials from account permission issues before asking for a new token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-keyword-picker)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown summaries with optional JSON examples, shell commands, and exported spreadsheet files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should lead with conclusions, label numeric data by marketplace and period, and export large record sets instead of pasting long tables.]

## Skill Version(s):

0.1.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
