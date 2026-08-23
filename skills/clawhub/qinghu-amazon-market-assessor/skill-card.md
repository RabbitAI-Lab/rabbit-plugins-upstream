## Description:

This skill helps Amazon sellers assess whether a niche category is worth entering by using Qinghu market data on sales volume, revenue, concentration, price bands, seller geography, new-product activity, demand trends, and return-rate risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and market analysts use this skill to evaluate Amazon category entry decisions before investing in a product line. It supports conclusion-first market assessments covering category size, competitive concentration, price opportunities, seller mix, new-product viability, demand direction, and key commercial risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require a Qinghu API token for third-party market data access.

Mitigation: Provide the token only when needed, prefer environment variables when available, and avoid exposing the token in prompts or shared outputs.

Risk: Qinghu API calls may consume paid credits.

Mitigation: Confirm user authorization before tool calls and report consumption using the returned envelope-level pointCost value.

Risk: Large result sets may be exported to local files that contain commercially sensitive market research.

Mitigation: Review generated exports before sharing them and handle local files according to the user's confidentiality requirements.

Risk: Market metrics are third-party estimates and can mislead if treated as exact figures.

Mitigation: Present figures with marketplace, time period, and sample context, and frame them as directional inputs for business review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-market-assessor)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown market assessment with optional exported spreadsheet files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conclusion-first output with market metrics, competitive structure, entry recommendations, risk list, and concise previews of exported data.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
