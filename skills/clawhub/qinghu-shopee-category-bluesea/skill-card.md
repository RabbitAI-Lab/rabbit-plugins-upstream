## Description:

青虎AI Shopee 类目蓝海挖掘 helps agents drill down through Shopee category levels, compare category rankings, trends, and price distribution, and identify high-growth, lower-competition niche categories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and marketplace analysts use this skill to evaluate Shopee sites and categories before opening a store or entering a new niche. It produces category recommendations based on market size, growth trends, competition concentration, and price-band opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for data access.

Mitigation: Provide the token through an approved secret source and avoid sharing it in conversation text or exported files.

Risk: Some Qinghu tool calls may consume paid points.

Mitigation: Confirm paid-tool authorization before calling non-free tools and report Qinghu point usage from the response envelope.

Risk: Large result sets may be exported to local spreadsheet files.

Mitigation: Use the skill only with data that is acceptable to store locally and review exported files before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-bluesea)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files]

**Output Format:** [Concise Markdown recommendations with links to exported tabular files when result sets are large.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include spreadsheet exports for record arrays with 10 or more rows and should report paid Qinghu point usage when applicable.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
