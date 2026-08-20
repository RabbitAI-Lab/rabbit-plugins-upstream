## Description:

Qinghu AI Amazon Trend Hunter helps agents use Qinghu API data to find current Amazon best sellers and rising products, validate historical trend signals, and flag product opportunity risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product researchers, and commerce operators use this skill to screen categories or keywords for strong-selling and rising products, then compare trend, competition, review, seller, and profitability signals before deciding what to investigate further.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a Qinghu API token and may expose that token to tool calls or request examples.

Mitigation: Use a scoped Qinghu token when possible, provide it through environment variables or secure tool configuration, and avoid sharing logs that include authorization headers.

Risk: Large product-research result sets may be exported to local files or links and can contain commercially sensitive research.

Mitigation: Review generated file paths and links before sharing them, and restrict access to exports that contain private product, market, or sourcing research.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-trend-hunter)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key management](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Files]

**Output Format:** [Markdown with JSON request examples and optional spreadsheet exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export larger product-research result sets to local files or links by default.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
