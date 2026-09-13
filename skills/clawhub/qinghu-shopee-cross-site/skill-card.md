## Description:

青虎AI Shopee 跨站点拓客帮助卖家用品牌和类目数据评估同类商品在多个 Shopee 站点的分布密度、存活情况和拓展优先级。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, marketplace operators, and ecommerce analysts use this skill to compare potential expansion sites, identify whether comparable brands or products already sell in those markets, and decide which Shopee site to open first.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a Qinghu API token, which could expose account access if mishandled.

Mitigation: Request the token only when needed, prefer environment variables such as QINGHU_TOKEN or QHKIT_TOKEN, and avoid echoing or storing the token in outputs.

Risk: Qinghu data calls may consume paid credits.

Mitigation: Confirm user authorization before making paid calls and report actual consumption from the Qinghu response envelope when available.

Risk: Exported spreadsheets may contain business research data.

Mitigation: Handle generated files as user business data and share only the intended export links and concise previews.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-cross-site)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files]

**Output Format:** [Markdown recommendations with optional spreadsheet export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs prioritize a site ranking, comparison table, localization notes, discouraged sites, and exported data files for record arrays with at least 10 entries.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
