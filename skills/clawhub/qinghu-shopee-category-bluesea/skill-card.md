## Description:

This skill guides agents through Qinghu-powered Shopee category research, drilling from top-level to third-level categories to compare market size, growth, competition, trends, and price bands for blue-ocean category recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketplace analysts, and agents use this skill to evaluate Shopee sites and categories, identify high-growth low-competition third-level niches, and produce concise category, price-band, and site recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a Qinghu API token and make authenticated network requests that may consume Qinghu credits.

Mitigation: Keep the token scoped to Qinghu use, review the planned tool list before approving calls, and require user confirmation before data-tool calls.

Risk: Larger Shopee result sets may be exported to local table files.

Mitigation: Avoid sensitive or unrelated local data and review exported files before sharing them.

Risk: Category recommendations depend on correct Qinghu tool parameters and successful nested API responses.

Mitigation: Check required input schemas, validate protocol and business-data success fields, and report missing permissions or parameters instead of substituting similar tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-bluesea)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown response with concise recommendations and optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For result arrays with at least 10 records, the skill expects table-file export plus a short preview instead of large inline tables.]

## Skill Version(s):

0.1.1 (source: evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
