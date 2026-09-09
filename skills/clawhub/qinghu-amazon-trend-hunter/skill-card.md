## Description:

青虎AI 亚马逊爆款趋势挖掘师 helps agents identify current best-selling and rising Amazon products using Qinghu data filters for sales, BSR growth, ratings, reviews, margin, seller structure, and historical trend signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and market researchers use this skill to scope Amazon marketplaces, filter product opportunities, validate trends, and rank candidates by opportunity rather than raw sales volume.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request or use a Qinghu API token and call an external Qinghu endpoint.

Mitigation: Provide credentials only through the documented token flow or environment variables, and review the planned API calls before authorizing them.

Risk: Qinghu API calls may consume Qinghu credits after user approval.

Mitigation: Confirm the planned tools before execution and report actual consumption from the returned pointCost value.

Risk: Product opportunity conclusions rely on third-party Amazon market estimates and trend signals.

Mitigation: Use the skill's trend-validation steps and cross-check high-impact decisions against additional business data before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-trend-hunter)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow credential check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with structured product fields, inline JSON examples, optional shell/API call snippets, and exported table files when result sets are large]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASINs, titles, prices, estimated monthly sales, BSR, ratings, review counts, seller counts, growth rates, concise recommendations, exclusion reasons, and Qinghu point-cost reporting.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
