## Description:

This skill helps agents assess whether an Amazon category is worth entering by using Qinghu market data to evaluate market size, concentration, price bands, seller geography, new-product activity, demand trends, and return-rate risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace operators, and agent-assisted analysts use this skill to decide whether to enter a category, where to position pricing, and which competitive risks need review before investing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send Amazon category or marketplace queries to Qinghu and requires a Qinghu API token.

Mitigation: Use a dedicated API key where possible and avoid including unrelated sensitive information in prompts or query parameters.

Risk: The skill may consume Qinghu credits when approved external data calls are made.

Mitigation: Review the proposed tools before authorizing calls and check reported pointCost-based consumption after use.

Risk: Market metrics are third-party estimates intended for comparison and trend analysis, not definitive financial forecasts.

Mitigation: Treat the skill output as decision support and verify costs, compliance, certification, patent, and launch assumptions independently.

## Reference(s):

- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-market-assessor)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, API Calls, Files, Guidance]

**Output Format:** [Markdown summary with optional exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs begin with an enter, cautious enter, or do not enter recommendation, followed by supporting market metrics, competitive structure, entry suggestions, and risk notes.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
