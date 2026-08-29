## Description:

Analyzes Ozon competitor shops through Qinghu data APIs to identify product mix, sales structure, trend snapshots, rising new products, and practical follow-up recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and analysts use this skill to study Ozon competitor shops, compare store performance, monitor new products, and produce actionable product-following and differentiation recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a Qinghu API token and may make paid Qinghu data calls.

Mitigation: Confirm user authorization before data calls, protect the token, and report Qinghu credit consumption from the returned pointCost value.

Risk: Exported shop and product data may contain sensitive business intelligence.

Mitigation: Review exported files for sensitive commercial data before sharing them outside the intended audience.

Risk: Competitor-copying recommendations can raise brand, patent, or marketplace-policy concerns.

Mitigation: Verify brand authorization, patent exposure, and Ozon marketplace policy risk before acting on product-following recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-intercept)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Files, Guidance]

**Output Format:** [Markdown summary with tables or exported spreadsheet files for larger datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should label numeric data with site, accounting period, cycle, and sample-size context.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
