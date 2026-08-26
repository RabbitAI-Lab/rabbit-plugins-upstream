## Description:

Analyzes a supplied Amazon ASIN or product link using Qinghu data to summarize product status, price and BSR trends, reviews, variants, fees, traffic keywords, order keywords, and competitive risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce analysts, and competitive research teams use this skill to evaluate a specified ASIN or Amazon product URL before decisions about following, pricing, listing optimization, or competitive positioning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for product analysis requests.

Mitigation: Provide or configure the token deliberately and avoid exposing it in chat output, logs, or exported files.

Risk: Qinghu tool calls may consume credits.

Mitigation: Review the skill's pre-call confirmation and reported credit usage before approving analysis calls.

Risk: Larger result sets may be written to local spreadsheet files.

Mitigation: Review exported file paths and contents before sharing them outside the local workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-asin-analyst)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key management](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown analysis with concise recommendations, optional API call details, and links to exported spreadsheet files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should lead with a recommendation, include source scope such as marketplace and sample size, and avoid dumping large raw datasets into chat.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
